import streamlit as st

# ===================== 1. 完全沿用你Flask内全部指标配置、权重、分级 =====================
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


# ===================== 2. Risk calculation =====================
RISK_COLORS = {
    "Extremely Low": "#2E7D32",
    "Low": "#7CB342",
    "Medium": "#F9A825",
    "High": "#EF6C00",
    "Extremely High": "#C62828",
}

DIMENSIONS = {
    "Source": {
        "icon": "🏭",
        "color": "#B84A33",
        "soft": "#FFF3EF",
        "display_name": "Source",
        "short_name": "Source",
        "description": "Coal Mining and Washing Enterprises",
    },
    "Pathway": {
        "icon": "🌧️",
        "color": "#1C6E8C",
        "soft": "#EEF8FC",
        "display_name": "Pathway",
        "short_name": "Pathway",
        "description": "Atmospheric transport, surface runoff, infiltration and migration conditions",
    },
    "Receptor": {
        "icon": "🌿",
        "color": "#4F772D",
        "soft": "#F2F8EC",
        "display_name": "Receptor",
        "short_name": "Receptor",
        "description": "Human exposure, farmland and ecological vulnerability",
    },
}


def normalize_indicator(indicator, value, boundary_mapping=True):
    """Normalize using the study range while leaving the input itself unrestricted."""
    ref_min = float(indicator["min"])
    ref_max = float(indicator["max"])
    if ref_max == ref_min:
        return 0.0

    value = float(value)
    if indicator["direction"] == "Positive":
        score = (value - ref_min) / (ref_max - ref_min)
    else:
        score = (ref_max - value) / (ref_max - ref_min)

    if boundary_mapping:
        score = min(max(score, 0.0), 1.0)
    return score


def classify_risk(score, risk_type):
    for rule in risk_level_rules:
        if rule["risk_type"] != risk_type:
            continue
        levels = rule["levels"]
        if score <= levels[0]["max"]:
            return levels[0]["level"]
        for level in levels[1:]:
            if score <= level["max"]:
                return level["level"]
        return levels[-1]["level"]
    return "Unknown"


def calculate_risk(inputs, boundary_mapping=True):
    dimension_scores = {"Source": 0.0, "Pathway": 0.0, "Receptor": 0.0}
    details = []

    for indicator in indicator_config:
        raw_value = inputs[indicator["name"]]
        normalized = normalize_indicator(indicator, raw_value, boundary_mapping)
        contribution = normalized * indicator["weight"]
        dimension_scores[indicator["dimension"]] += contribution
        details.append({
            "indicator": indicator["name"],
            "dimension": indicator["dimension"],
            "input": raw_value,
            "normalized": normalized,
            "weight": indicator["weight"],
            "contribution": contribution,
        })

    comprehensive = sum(dimension_scores.values())
    dominant = max(dimension_scores, key=dimension_scores.get)

    return {
        "dimension_scores": dimension_scores,
        "comprehensive": comprehensive,
        "levels": {
            "Source": classify_risk(dimension_scores["Source"], "Source"),
            "Pathway": classify_risk(dimension_scores["Pathway"], "Pathway"),
            "Receptor": classify_risk(dimension_scores["Receptor"], "Receptor"),
            "Comprehensive": classify_risk(comprehensive, "Comprehensive"),
        },
        "dominant": dominant,
        "details": sorted(details, key=lambda row: row["contribution"], reverse=True),
    }


# ===================== 3. Page configuration =====================
st.set_page_config(
    page_title="Environmental Risk Assessment System for Coal Mining and Washing Enterprises",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root {
        --navy:#153B55;
        --blue:#1C6E8C;
        --green:#4F772D;
        --rust:#B84A33;
        --ink:#20313D;
        --muted:#667A88;
        --line:#DDE7EC;
    }

    .stApp {
        background:
          radial-gradient(circle at 96% 0%, rgba(28,110,140,.10), transparent 28%),
          linear-gradient(180deg,#EFF7FB 0%,#FFFFFF 24%,#FFFFFF 100%);
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1480px;
        padding-top: 1.2rem;
        padding-bottom: 4rem;
    }

    .v2-banner {
        border:1px solid #D7E5EC;
        border-radius:24px;
        padding:1.6rem 1.8rem 1.45rem;
        background:
          radial-gradient(circle at 92% 14%, rgba(79,119,45,.12), transparent 26%),
          linear-gradient(135deg,#FFFFFF 0%,#EEF8FC 58%,#F5F9F1 100%);
        box-shadow:0 12px 34px rgba(21,59,85,.09);
        margin-bottom:1rem;
    }
    .v2-tag {
        display:inline-block;
        padding:.28rem .62rem;
        border-radius:999px;
        background:#153B55;
        color:white;
        font-size:.76rem;
        font-weight:800;
        letter-spacing:.08em;
        margin-bottom:.65rem;
    }
    .v2-banner h1 {
        color:#153B55;
        font-size:clamp(1.85rem,3vw,2.85rem);
        line-height:1.12;
        margin:0 0 .5rem;
        letter-spacing:-.03em;
    }
    .v2-banner p {
        color:#586F7D;
        font-size:1.02rem;
        margin:0;
        max-width:1050px;
    }
    .stats-row {
        display:flex;
        flex-wrap:wrap;
        gap:.55rem;
        margin-top:1rem;
    }
    .stat-chip {
        padding:.48rem .76rem;
        border:1px solid #D5E3EA;
        border-radius:999px;
        background:rgba(255,255,255,.88);
        color:#294B60;
        font-size:.84rem;
        font-weight:700;
    }

    .notice {
        border-left:5px solid #1C6E8C;
        border-radius:0 14px 14px 0;
        background:#EEF8FC;
        padding:.9rem 1rem;
        margin:.45rem 0 1rem;
        color:#3E5C6B;
    }

    .dimension-head {
        padding:.9rem 1rem;
        border-radius:16px;
        border:1px solid #DFE8EC;
        margin:.3rem 0 .9rem;
    }
    .dimension-title {
        font-size:1.15rem;
        font-weight:850;
        color:#153B55;
    }
    .dimension-desc {
        margin-top:.15rem;
        color:#687B87;
        font-size:.88rem;
    }

    div[data-testid="stForm"] {
        border:1px solid #DCE6EB;
        border-radius:22px;
        padding:1.05rem 1.15rem 1.3rem;
        background:rgba(255,255,255,.94);
        box-shadow:0 9px 25px rgba(29,54,71,.055);
    }
    button[data-baseweb="tab"] {
        font-weight:800;
        font-size:.98rem;
    }
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        font-weight:700;
        color:#294652;
    }
    div[data-baseweb="input"],
    div[data-baseweb="select"] > div {
        border-radius:12px;
    }
    div[data-testid="stFormSubmitButton"] button {
        width:100%;
        min-height:3.1rem;
        border:none;
        border-radius:14px;
        font-weight:850;
        background:linear-gradient(90deg,#1C6E8C,#245B7A);
        box-shadow:0 8px 18px rgba(28,110,140,.22);
    }

    .reference-pill {
        display:inline-block;
        margin-top:-.15rem;
        margin-bottom:.45rem;
        padding:.18rem .46rem;
        border-radius:999px;
        background:#F3F6F8;
        color:#74838D;
        font-size:.72rem;
        border:1px solid #E4EAED;
    }

    .result-card {
        border:1px solid #DCE6EB;
        border-radius:18px;
        padding:1.05rem 1.1rem;
        background:white;
        box-shadow:0 8px 22px rgba(25,49,66,.06);
        min-height:160px;
    }
    .result-card .label {
        color:#687A86;
        font-size:.78rem;
        font-weight:800;
        text-transform:uppercase;
        letter-spacing:.06em;
    }
    .result-card .score {
        color:#153B55;
        font-size:2rem;
        font-weight:900;
        margin:.35rem 0 .7rem;
    }
    .risk-badge {
        display:inline-block;
        padding:.34rem .65rem;
        color:white;
        border-radius:999px;
        font-size:.79rem;
        font-weight:850;
    }
    .dominant {
        margin-top:.9rem;
        padding:1rem 1.1rem;
        border:1px solid #D8E6E3;
        border-radius:16px;
        background:linear-gradient(90deg,#EEF8FC,#F3F8EC);
        color:#294B59;
    }
    .bar-row {
        display:grid;
        grid-template-columns:minmax(170px,1.35fr) 4fr 74px;
        gap:.7rem;
        align-items:center;
        margin:.58rem 0;
    }
    .bar-track {
        height:11px;
        border-radius:999px;
        overflow:hidden;
        background:#E8EEF1;
    }
    .bar-fill {height:100%;border-radius:999px;}
    .muted {color:#6A7D88;font-size:.8rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


# ===================== 4. Header and settings =====================
st.markdown(
    """
    <div class="v2-banner">
      <h1>Environmental Risk Assessment System for Coal Mining and Washing Enterprises</h1>
      <p>An SPR-based screening tool using AHP–CRITIC integrated weights for rapid environmental risk assessment.</p>
      <div class="stats-row">
        <span class="stat-chip">📋 25 indicators</span>
        <span class="stat-chip">🧭 Source–Pathway–Receptor</span>
        <span class="stat-chip">⚖️ AHP–CRITIC weighting</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Continuous fields remain unrestricted, while normalized scores are mapped to
# the calibrated 0–1 range in the backend to preserve the published model.
boundary_mapping = True

st.markdown(
    """
    <div class="notice">
      <b>Warm Prompt</b><br>
      1. This system evaluates the environmental risk of coal mining and washing enterprises using the Source–Pathway–Receptor framework.<br>
      2. The 25 indicators are organized into three modules: Source, Pathway, and Receptor.<br>
      3. Indicator weights were determined using the integrated AHP–CRITIC method and are embedded in the calculation program.<br>
      4. Please complete all input fields before calculation. If a value is uncertain or unavailable, enter <b>0</b>.
    </div>
    """,
    unsafe_allow_html=True,
)

source_items = [x for x in indicator_config if x["dimension"] == "Source"]
pathway_items = [x for x in indicator_config if x["dimension"] == "Pathway"]
receptor_items = [x for x in indicator_config if x["dimension"] == "Receptor"]


def render_inputs(items, dimension):
    meta = DIMENSIONS[dimension]
    st.markdown(
        f"""
        <div class="dimension-head" style="border-left:5px solid {meta['color']};background:{meta['soft']};">
          <div class="dimension-title">{meta['icon']} {meta.get('display_name', dimension)}</div>
          <div class="dimension-desc">{meta['description']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    output = {}
    cols = st.columns(2, gap="large")
    for idx, item in enumerate(items):
        with cols[idx % 2]:
            widget_key = f"v5_{dimension}_{idx}"
            if item["type"] == "Categorical":
                labels = [opt["label"] for opt in item["options"]]
                selected = st.selectbox(
                    item["name"],
                    labels,
                    key=widget_key,
                    help=f"Weight: {item['weight']:.4f} · Direction: {item['direction']}",
                )
                value_map = {opt["label"]: opt["value"] for opt in item["options"]}
                output[item["name"]] = value_map[selected]
            else:
                unit = f" ({item['unit']})" if item["unit"] else ""
                value = st.number_input(
                    f"{item['name']}{unit}",
                    value=0.0,
                    step=0.01,
                    format="%.4f",
                    key=widget_key,
                    help=(
                        f"Reference range: {item['min']}–{item['max']} · "
                        f"Weight: {item['weight']:.4f} · Direction: {item['direction']} · "
                        "Input is unrestricted."
                    ),
                )
                st.markdown(
                    f"<span class='reference-pill'>Reference only: {item['min']} – {item['max']}</span>",
                    unsafe_allow_html=True,
                )
                output[item["name"]] = value
    return output


# ===================== 5. Input form =====================
with st.form("cmwe_v5_form", clear_on_submit=False):
    tab_source, tab_pathway, tab_receptor = st.tabs(
        ["01 · Source", "02 · Pathway", "03 · Receptor"]
    )
    with tab_source:
        source_values = render_inputs(source_items, "Source")
    with tab_pathway:
        pathway_values = render_inputs(pathway_items, "Pathway")
    with tab_receptor:
        receptor_values = render_inputs(receptor_items, "Receptor")

    st.markdown("---")
    submitted = st.form_submit_button("Calculate environmental risk")


# ===================== 6. Results =====================
if submitted:
    user_inputs = {**source_values, **pathway_values, **receptor_values}
    result = calculate_risk(user_inputs, boundary_mapping=boundary_mapping)

    st.markdown("## Risk assessment results")
    st.caption("Model outputs are based on the integrated indicator weights and the selected normalization handling mode.")

    cards = [
        ("Source", result["dimension_scores"]["Source"], result["levels"]["Source"]),
        ("Pathway", result["dimension_scores"]["Pathway"], result["levels"]["Pathway"]),
        ("Receptor", result["dimension_scores"]["Receptor"], result["levels"]["Receptor"]),
        ("Comprehensive", result["comprehensive"], result["levels"]["Comprehensive"]),
    ]

    columns = st.columns(4)
    for col, (name, score, level) in zip(columns, cards):
        with col:
            color = RISK_COLORS.get(level, "#607D8B")
            st.markdown(
                f"""
                <div class="result-card">
                  <div class="label">{name} risk</div>
                  <div class="score">{score:.6f}</div>
                  <span class="risk-badge" style="background:{color};">{level}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    dominant_meta = DIMENSIONS[result["dominant"]]
    st.markdown(
        f"""
        <div class="dominant"><b>{dominant_meta['icon']} Dominant dimension:</b> <span style="color:{dominant_meta['color']};font-weight:900;">{result['dominant']}</span> · score = <b>{result['dimension_scores'][result['dominant']]:.6f}</b></div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown("### Dimension contribution shares")
        total = max(result["comprehensive"], 1e-12)
        for dimension in ["Source", "Pathway", "Receptor"]:
            value = result["dimension_scores"][dimension]
            share = value / total * 100.0
            meta = DIMENSIONS[dimension]
            st.markdown(
                f"""
                <div class="bar-row">
                  <div><b>{meta['icon']} {meta.get('short_name', dimension)}</b></div>
                  <div class="bar-track"><div class="bar-fill" style="width:{min(max(share,0),100):.2f}%;background:{meta['color']};"></div></div>
                  <div style="text-align:right;font-weight:800;">{share:.1f}%</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with right:
        st.markdown("### Leading indicator contributions")
        top_items = result["details"][:6]
        max_contribution = max([row["contribution"] for row in top_items] + [1e-12])
        for row in top_items:
            meta = DIMENSIONS[row["dimension"]]
            width = row["contribution"] / max_contribution * 100.0
            st.markdown(
                f"""
                <div class="bar-row">
                  <div><b>{row['indicator']}</b><div class="muted">{row['dimension']} · weight {row['weight']:.4f}</div></div>
                  <div class="bar-track"><div class="bar-fill" style="width:{min(max(width,0),100):.2f}%;background:{meta['color']};"></div></div>
                  <div style="text-align:right;font-weight:800;">{row['contribution']:.4f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
