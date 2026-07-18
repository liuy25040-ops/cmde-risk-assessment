import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# =====================================================
# Page Config
# =====================================================
st.set_page_config(
    page_title="Environmental Risk Assessment System for Coal Mining and Washing Enterprises",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CSS（SCI风格）
# =====================================================
st.markdown("""
<style>
.main{
    padding-top:1rem;
}
.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    max-width:1450px;
}
/* Title */
.big-title{
    font-size:40px;
    font-weight:700;
    color:#163A5F;
    margin-bottom:0px;
}
.subtitle{
    color:#666666;
    font-size:17px;
    margin-top:-10px;
    margin-bottom:20px;
}
/* Section */
.section-title{
    font-size:26px;
    font-weight:700;
    color:#184A73;
    margin-top:20px;
    margin-bottom:15px;
}
/* Card */
.card{
    background:white;
    padding:18px;
    border-radius:15px;
    border:1px solid #E6E9EF;
    box-shadow:0 3px 10px rgba(0,0,0,.05);
}
/* Result Card */
.result-card{
    background:#F8FBFF;
    border-left:6px solid #2E86DE;
    padding:15px;
    border-radius:10px;
}
/* Button */
.stButton>button{
    width:100%;
    height:52px;
    border-radius:10px;
    font-size:18px;
    font-weight:700;
}
/* Metric */
[data-testid="metric-container"]{
    border:1px solid #EEEEEE;
    padding:15px;
    border-radius:12px;
    background:white;
}
/* Divider */
hr{
    margin-top:25px;
    margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

indicator_config = [
    # Source Dimension
    {
        "name": "Enterprise scale",
        "cn_name": "Enterprise scale",
        "dimension": "Source",
        "type": "Categorical",
        "options": [
            {"value": 4, "label": "Large-scale"},
            {"value": 3, "label": "Medium-scale"},
            {"value": 2, "label": "Small-scale"},
            {"value": 1, "label": "Micro-scale"}
        ],
        "min": 1,
        "max": 4,
        "direction": "Positive",
        "weight": 0.0716,
        "unit": ""
    },
    {
        "name": "Business status",
        "cn_name": "Enterprise operation status",
        "dimension": "Source",
        "type": "Categorical",
        "options": [
            {"value": 4, "label": "In Production"},
            {"value": 3, "label": "Shut Down"},
            {"value": 2, "label": "Revoked"},
            {"value": 1, "label": "Cancelled"}
        ],
        "min": 1,
        "max": 4,
        "direction": "Positive",
        "weight": 0.0337,
        "unit": ""
    },
    {
        "name": "Operation duration",
        "cn_name": "Operation duration",
        "dimension": "Source",
        "type": "Continuous",
        "min": 0,
        "max": 74,
        "direction": "Positive",
        "weight": 0.0430,
        "unit": "a"
    },
    {
        "name": "Mining method",
        "cn_name": "Mining method",
        "dimension": "Source",
        "type": "Categorical",
        "options": [
            {"value": 3, "label": "Open-pit & Combined mining"},
            {"value": 2, "label": "Underground mining"},
            {"value": 1, "label": "Only coal washing, no mining"}
        ],
        "min": 1,
        "max": 3,
        "direction": "Positive",
        "weight": 0.0441,
        "unit": ""
    },
    {
        "name": "Mining field area",
        "cn_name": "Mining field area",
        "dimension": "Source",
        "type": "Continuous",
        "min": 0,
        "max": 8323,
        "direction": "Positive",
        "weight": 0.0306,
        "unit": "km²"
    },
    {
        "name": "Number of discharge outlets",
        "cn_name": "Number of discharge outlets",
        "dimension": "Source",
        "type": "Continuous",
        "min": 0,
        "max": 87,
        "direction": "Positive",
        "weight": 0.0501,
        "unit": ""
    },
    {
        "name": "Located in industrial park",
        "cn_name": "Industrial park location",
        "dimension": "Source",
        "type": "Categorical",
        "options": [
            {"value": 1, "label": "Yes"},
            {"value": 0, "label": "No"}
        ],
        "min": 0,
        "max": 1,
        "direction": "Negative",
        "weight": 0.0392,
        "unit": ""
    },
    {
        "name": "Environmental regulatory records",
        "cn_name": "Environmental supervision records",
        "dimension": "Source",
        "type": "Continuous",
        "min": 0,
        "max": 56,
        "direction": "Positive",
        "weight": 0.0768,
        "unit": ""
    },
    {
        "name": "Enterprise supervision level",
        "cn_name": "Enterprise supervision level",
        "dimension": "Source",
        "type": "Categorical",
        "options": [
            {"value": 3, "label": "National/Provincial key supervision"},
            {"value": 2, "label": "Municipal key supervision only"},
            {"value": 1, "label": "Not included in key supervision"}
        ],
        "min": 1,
        "max": 3,
        "direction": "Positive",
        "weight": 0.0825,
        "unit": ""
    },
    # Pathway Dimension
    {
        "name": "Impervious surface ratio",
        "cn_name": "Impervious surface ratio",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": 0,
        "max": 0.98,
        "direction": "Positive",
        "weight": 0.0324,
        "unit": "%"
    },
    {
        "name": "Annual average precipitation",
        "cn_name": "Annual average precipitation",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": 30.79,
        "max": 1831.64,
        "direction": "Positive",
        "weight": 0.0498,
        "unit": "mm"
    },
    {
        "name": "Terrain slope",
        "cn_name": "Terrain slope",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": 0.21,
        "max": 17.26,
        "direction": "Positive",
        "weight": 0.0474,
        "unit": "°"
    },
    {
        "name": "River network density",
        "cn_name": "River network density",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": 0,
        "max": 0.49,
        "direction": "Positive",
        "weight": 0.0443,
        "unit": "km/km²"
    },
    {
        "name": "Soil erosion intensity",
        "cn_name": "Soil erosion intensity",
        "dimension": "Pathway",
        "type": "Categorical",
        "options": [
            {"value": 6, "label": "Severe erosion"},
            {"value": 5, "label": "Extremely strong erosion"},
            {"value": 4, "label": "Strong erosion"},
            {"value": 3, "label": "Moderate erosion"},
            {"value": 2, "label": "Light erosion"},
            {"value": 1, "label": "Slight erosion"}
        ],
        "min": 1,
        "max": 6,
        "direction": "Positive",
        "weight": 0.0403,
        "unit": ""
    },
    {
        "name": "Groundwater depth",
        "cn_name": "Groundwater depth",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": -5.42,
        "max": 2634.89,
        "direction": "Negative",
        "weight": 0.0498,
        "unit": "m"
    },
    {
        "name": "Clay Content in Soil Texture",
        "cn_name": "Soil clay content",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": 3,
        "max": 68,
        "direction": "Positive",
        "weight": 0.0197,
        "unit": "%"
    },
    {
        "name": "Annual average wind speed",
        "cn_name": "Annual average wind speed",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": 1.36,
        "max": 4.36,
        "direction": "Positive",
        "weight": 0.0200,
        "unit": "m/s"
    },
    {
        "name": "Annual average temperature",
        "cn_name": "Annual average temperature",
        "dimension": "Pathway",
        "type": "Continuous",
        "min": -1.66,
        "max": 25.11,
        "direction": "Positive",
        "weight": 0.0169,
        "unit": "℃"
    },
    # Receptor Dimension
    {
        "name": "Population density",
        "cn_name": "Population density",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 0.16,
        "max": 10961.75,
        "direction": "Positive",
        "weight": 0.0302,
        "unit": "people/km²"
    },
    {
        "name": "Age structure",
        "cn_name": "Age structure proportion",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 18.66,
        "max": 41.70,
        "direction": "Positive",
        "weight": 0.0217,
        "unit": "%"
    },
    {
        "name": "Surrounding sensitive targets number",
        "cn_name": "Number of surrounding sensitive targets",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 53,
        "max": 19995,
        "direction": "Positive",
        "weight": 0.0308,
        "unit": ""
    },
    {
        "name": "Water system length",
        "cn_name": "Water system length",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 0.77,
        "max": 12943.16,
        "direction": "Positive",
        "weight": 0.0311,
        "unit": "km"
    },
    {
        "name": "Farmland area",
        "cn_name": "Farmland area",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 0.19,
        "max": 6064.05,
        "direction": "Positive",
        "weight": 0.0288,
        "unit": "km²"
    },
    {
        "name": "Vegetation coverage",
        "cn_name": "Vegetation coverage",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 0,
        "max": 99.82,
        "direction": "Negative",
        "weight": 0.0337,
        "unit": "%"
    },
    {
        "name": "Normalized Difference Vegetation Index (NDVI)",
        "cn_name": "NDVI",
        "dimension": "Receptor",
        "type": "Continuous",
        "min": 0.06,
        "max": 0.74,
        "direction": "Negative",
        "weight": 0.0316,
        "unit": ""
    }
]

risk_level_rules = [
    {
        "risk_type": "Source",
        "levels": [
            {"level": "Extremely Low", "min": 0.039021, "max": 0.124448},
            {"level": "Low", "min": 0.124449, "max": 0.167270},
            {"level": "Medium", "min": 0.167271, "max": 0.205180},
            {"level": "High", "min": 0.205181, "max": 0.243815},
            {"level": "Extremely High", "min": 0.243816, "max": 0.361208}
        ]
    },
    {
        "risk_type": "Pathway",
        "levels": [
            {"level": "Extremely Low", "min": 0.071172, "max": 0.097543},
            {"level": "Low", "min": 0.097544, "max": 0.115646},
            {"level": "Medium", "min": 0.115647, "max": 0.129964},
            {"level": "High", "min": 0.129965, "max": 0.148026},
            {"level": "Extremely High", "min": 0.148027, "max": 0.192598}
        ]
    },
    {
        "risk_type": "Receptor",
        "levels": [
            {"level": "Extremely Low", "min": 0.017387, "max": 0.030667},
            {"level": "Low", "min": 0.030668, "max": 0.039351},
            {"level": "Medium", "min": 0.039352, "max": 0.052298},
            {"level": "High", "min": 0.052299, "max": 0.070748},
            {"level": "Extremely High", "min": 0.070749, "max": 0.106305}
        ]
    },
    {
        "risk_type": "Comprehensive",
        "levels": [
            {"level": "Extremely Low", "min": 0.186889, "max": 0.284958},
            {"level": "Low", "min": 0.284959, "max": 0.335912},
            {"level": "Medium", "min": 0.335913, "max": 0.379298},
            {"level": "High", "min": 0.379299, "max": 0.423406},
            {"level": "Extremely High", "min": 0.423407, "max": 0.521760}
        ]
    }
]


# ===================== 核心计算逻辑 =====================
def calculate_indicator_score(indicator, input_value):
    # 已移除数值强制截断，输入值可超出原范围
    if indicator['direction'] == 'Positive':
        score = (input_value - indicator['min']) / (indicator['max'] - indicator['min'])
    else:
        score = (indicator['max'] - input_value) / (indicator['max'] - indicator['min'])
    return score


def get_risk_level(score, risk_type):
    for rule in risk_level_rules:
        if rule['risk_type'] == risk_type:
            for level in rule['levels']:
                if level['min'] <= score <= level['max']:
                    return level["level"]
    return "Unknown"


def calculate_risk(input_dict):
    dimension_scores = {"Source": 0, "Pathway": 0, "Receptor": 0}
    for ind in indicator_config:
        name = ind["name"]
        val = input_dict[name]
        single_score = calculate_indicator_score(ind, val)
        dimension_scores[ind["dimension"]] += single_score * ind["weight"]

    comp_score = sum(dimension_scores.values())
    res = {}
    res["Source_score"] = round(dimension_scores["Source"], 6)
    res["Source_level"] = get_risk_level(dimension_scores["Source"], "Source")
    res["Pathway_score"] = round(dimension_scores["Pathway"], 6)
    res["Pathway_level"] = get_risk_level(dimension_scores["Pathway"], "Pathway")
    res["Receptor_score"] = round(dimension_scores["Receptor"], 6)
    res["Receptor_level"] = get_risk_level(dimension_scores["Receptor"], "Receptor")
    res["Comprehensive_score"] = round(comp_score, 6)
    res["Comprehensive_level"] = get_risk_level(comp_score, "Comprehensive")

    max_s = -1
    dom_dim = ""
    for d in dimension_scores:
        if dimension_scores[d] > max_s:
            max_s = dimension_scores[d]
            dom_dim = d
    res["Dominant_dimension"] = dom_dim
    res["Dominant_score"] = round(max_s, 6)
    return res


# ===================== Streamlit 页面布局 =====================
st.set_page_config(page_title="Environmental Risk Assessment System for Coal Mining and Washing Enterprises",
                   layout="wide")

# 主标题
st.title("Environmental Risk Assessment System for Coal Mining and Washing Enterprises")
st.caption("Quantitative Pollution Risk Evaluation Tool")

# 温馨提示框
st.info("""
**Warm Prompt**
1. This system adopts official national data of coal mining and washing enterprises collected in 2025 to assess the current pollution risk status of enterprises.
2. All evaluation indicators are divided into three independent modules: Source, Pathway and Receptor.
3. The comprehensive weight of each indicator is calculated by the coupled AHP-CRITIC method and solidified in the backend program. Users only need to fill in parameters to automatically obtain risk scores and risk grades.
4. Please fill in all input boxes before clicking the calculation button. If the information is uncertain, please enter 0.
""")

# 按维度分组指标
source_list = [i for i in indicator_config if i["dimension"] == "Source"]
path_list = [i for i in indicator_config if i["dimension"] == "Pathway"]
recep_list = [i for i in indicator_config if i["dimension"] == "Receptor"]

input_storage = {}

# Source 输入区
st.subheader("Source Dimension Indicators")
src_cols = st.columns(4)
idx = 0
for item in source_list:
    with src_cols[idx % 4]:
        if item["type"] == "Categorical":
            label_list = [opt["label"] for opt in item["options"]]
            val_list = [opt["value"] for opt in item["options"]]
            sel_label = st.selectbox(label=item["name"], options=label_list)
            real_val = val_list[label_list.index(sel_label)]
        else:
            real_val = st.number_input(
                label=f"{item['name']} ({item['unit']})",
                value=float(item["min"]),
                step=0.01
            )
        input_storage[item["name"]] = real_val
    idx += 1

st.divider()

# Pathway 输入区
st.subheader("Pathway Dimension Indicators")
path_cols = st.columns(4)
idx = 0
for item in path_list:
    with path_cols[idx % 4]:
        if item["type"] == "Categorical":
            label_list = [opt["label"] for opt in item["options"]]
            val_list = [opt["value"] for opt in item["options"]]
            sel_label = st.selectbox(label=item["name"], options=label_list)
            real_val = val_list[label_list.index(sel_label)]
        else:
            real_val = st.number_input(
                label=f"{item['name']} ({item['unit']})",
                value=float(item["min"]),
                step=0.01
            )
        input_storage[item["name"]] = real_val
    idx += 1

st.divider()

# Receptor 输入区
st.subheader("Receptor Dimension Indicators")
rec_cols = st.columns(4)
idx = 0
for item in recep_list:
    with rec_cols[idx % 4]:
        if item["type"] == "Categorical":
            label_list = [opt["label"] for opt in item["options"]]
            val_list = [opt["value"] for opt in item["options"]]
            sel_label = st.selectbox(label=item["name"], options=label_list)
            real_val = val_list[label_list.index(sel_label)]
        else:
            real_val = st.number_input(
                label=f"{item['name']} ({item['unit']})",
                value=float(item["min"]),
                step=0.01
            )
        input_storage[item["name"]] = real_val
    idx += 1

st.divider()

# 计算按钮
calc_button = st.button("Calculate Risk Score & Risk Level", type="primary")

# 结果展示区域
if calc_button:
    with st.spinner("Calculating risk index, please wait..."):
        res_data = calculate_risk(input_storage)
    st.success("Calculation Completed! Risk Assessment Output Results")

    res_cols = st.columns(4)
    with res_cols[0]:
        st.metric("Source Risk Score", value=res_data["Source_score"])
        st.markdown(f"Risk Level: **{res_data['Source_level']}**")
    with res_cols[1]:
        st.metric("Pathway Risk Score", value=res_data["Pathway_score"])
        st.markdown(f"Risk Level: **{res_data['Pathway_level']}**")
    with res_cols[2]:
        st.metric("Receptor Risk Score", value=res_data["Receptor_score"])
        st.markdown(f"Risk Level: **{res_data['Receptor_level']}**")
    with res_cols[3]:
        st.metric("Comprehensive Risk Score", value=res_data["Comprehensive_score"])
        st.markdown(f"Risk Level: **{res_data['Comprehensive_level']}**")

    st.info(
        f"**Dominant Risk Dimension**: {res_data['Dominant_dimension']} Dimension, Dimension Score = {res_data['Dominant_score']}")
