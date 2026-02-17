import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Carbon-Aware Cloud Decision Tool (v1)", layout="wide")

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "regions.csv"

DEFAULT_PUE = 1.15
DEFAULT_CARBON_PRICE = 100

WORKLOAD_PRESETS = {
    "Small App / API": 150,
    "Data Pipeline": 1500,
    "ML Inference (GPU)": 8000,
    "Custom": 1000,
}

def compute(df, kwh_month, pue, carbon_price):
    out = df.copy()
    out["monthly_tco2e"] = (kwh_month * pue * out["intensity_gco2e_per_kwh"]) / 1_000_000
    out["annual_tco2e"] = out["monthly_tco2e"] * 12
    out["annual_carbon_cost_eur"] = out["annual_tco2e"] * carbon_price
    out = out.sort_values("annual_tco2e", ascending=True).reset_index(drop=True)
    out["rank_cleanest"] = out.index + 1
    return out

df = pd.read_csv(DATA_PATH)

st.title("🎯 Carbon-Aware Cloud Deployment Decision Tool (v1)")
st.caption("Decision-support for sustainability managers evaluating carbon-aware cloud region strategies.")

st.sidebar.header("Workload Parameters")

preset = st.sidebar.selectbox("Workload preset", list(WORKLOAD_PRESETS.keys()))
kwh_month = st.sidebar.number_input(
    "Monthly workload energy (kWh)",
    min_value=1.0,
    value=float(WORKLOAD_PRESETS[preset]),
    step=50.0,
)

pue = st.sidebar.slider("PUE", 1.0, 2.0, DEFAULT_PUE, step=0.01)
carbon_price = st.sidebar.number_input(
    "Internal carbon price (€/tCO₂e)",
    min_value=0.0,
    value=float(DEFAULT_CARBON_PRICE),
    step=10.0
)

result = compute(df, kwh_month, pue, carbon_price)

best = result.iloc[0]
worst = result.iloc[-1]

annual_savings = worst["annual_tco2e"] - best["annual_tco2e"]
avoided_cost = annual_savings * carbon_price

col1, col2, col3 = st.columns(3)
col1.metric("Optimal Region", best["region_label"])
col2.metric("Annual Savings (vs highest)", f"{annual_savings:.2f} tCO₂e")
col3.metric("Avoided Carbon Cost", f"€{avoided_cost:,.0f}")

st.subheader("Annual Emissions Comparison")
fig = px.bar(result, x="region_label", y="annual_tco2e")
st.plotly_chart(fig, use_container_width=True)

with st.expander("Methodology"):
    st.write("""
    Formula:
    tCO₂e = (kWh × PUE × gCO₂e/kWh) / 1,000,000

    Intensity values are generation-based and sourced from EEA (2023).
    """)
