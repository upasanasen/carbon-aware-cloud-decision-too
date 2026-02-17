# Carbon-Aware Cloud Deployment Decision Tool (v1)

A decision-support system for corporate sustainability teams to optimize cloud region selection using **Scope 2 location-based** emission factors and **internal carbon pricing**.

✅ Live app: https://carbon-aware-cloud-tool.streamlit.app

---

## Why this matters

As cloud workloads grow (especially with AI), **where** you deploy can significantly change emissions because electricity grids differ by country.  
Sustainability teams need a simple way to quantify:

- **Estimated annual emissions** per cloud region
- **Avoided emissions** by switching to a lower-carbon region
- **Carbon cost exposure** using an internal carbon price (€ / tCO₂e)

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
