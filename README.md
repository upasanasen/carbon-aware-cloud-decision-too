# Carbon-Aware Cloud Deployment Decision Tool (V2)

A decision-support system for sustainability and cloud strategy teams to evaluate carbon-aware deployment across major cloud providers.

The tool compares cloud regions using electricity grid carbon intensity, data center efficiency, and internal carbon pricing to help organizations choose lower-emission infrastructure locations.

✅ Live app: https://carbon-aware-cloud-tool.streamlit.app

---

## Why this matters

As cloud workloads grow (especially with AI), **where** you deploy can significantly change emissions because electricity grids differ by country.  
Sustainability teams need a simple way to quantify:

- **Estimated annual emissions** per cloud region
- **Avoided emissions** by switching to a lower-carbon region
- **Carbon cost exposure** using an internal carbon price (€ / tCO₂e)

As AI workloads and cloud computing expand rapidly, the location of compute infrastructure has a significant impact on Scope 2 emissions.

This tool demonstrates how sustainability teams can integrate carbon-aware decision-making into infrastructure strategy, supporting:

- Internal carbon pricing
- EU ETS cost modeling
- ESG reporting and decarbonization planning
- Sustainable cloud architecture
---

## What the tool does

### Inputs
- Workload energy (kWh/month) — presets + custom
- Data center efficiency (PUE)
- Internal carbon price (€/tCO₂e)

### Outputs
- **Optimal region (lowest annual tCO₂e)**
- **Annual savings vs highest-intensity region**
- **Avoided carbon cost**
- Regional comparison chart

## New in Version 2

- Multi-cloud comparison (AWS, Azure, GCP)
- Cloud provider filtering
- Carbon price scenario analysis
- CSV export for sustainability reporting
- Interactive emissions map across Europe

---

## Methodology (v1)

**Annual tCO₂e** is calculated using:

tCO₂e = (kWh × PUE × gCO₂e/kWh) ÷ 1,000,000

- Grid intensity factors are stored in `data/regions.csv`
- This prototype uses **generation-based** grid intensity values (EEA, 2023)

---

## Data sources

- **EEA (European Environment Agency)** – grid emission intensity indicator (2023 averages)
- Region list is mapped to AWS EU regions for comparison

---

## Repo structure

```text
.
├── app/
│   └── app.py
├── data/
│   └── regions.csv
├── requirements.txt
└── README.md
