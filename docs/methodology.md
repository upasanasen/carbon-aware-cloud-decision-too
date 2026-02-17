# Methodology & Assumptions

## 1. Scope Definition

This prototype evaluates **Scope 2 location-based emissions** for cloud workloads deployed in European AWS regions.

It does NOT calculate:
- Scope 1 emissions
- Scope 3 embodied emissions (hardware manufacturing)
- Market-based Scope 2 (PPAs / RECs)

---

## 2. Emission Factor Approach

Emission intensity values are:

- Annual country-average generation-based grid intensity (gCO₂e/kWh)
- Based on European Environment Agency (EEA) data (2023)

These are mapped to AWS regions by country.

---

## 3. Calculation Formula

Annual emissions (tCO₂e):

tCO₂e = (Monthly kWh × 12 × PUE × grid_intensity) / 1,000,000

Where:

- kWh = IT energy consumption
- PUE = Power Usage Effectiveness
- grid_intensity = gCO₂e per kWh

---

## 4. Carbon Cost Estimation

Avoided carbon cost is calculated using:

Avoided Cost = Emissions Saved (tCO₂e) × Internal Carbon Price (€/tCO₂e)

This reflects internal carbon pricing mechanisms used by corporations.

---

## 5. Limitations

- Uses static annual averages (not hourly marginal factors)
- Does not include workload latency constraints
- Does not include renewable energy procurement strategies

---

## 6. Future Enhancements

- Add time-based grid intensity (marginal signals)
- Add Azure & Google Cloud regions
- Add embodied carbon estimates
- Add scenario stress testing
