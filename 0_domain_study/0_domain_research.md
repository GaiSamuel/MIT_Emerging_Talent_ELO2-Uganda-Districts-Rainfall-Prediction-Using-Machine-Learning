# 🌍 Domain Research: Uganda Rainfall & Climate Resilience

**Primary Source:** Uganda National Meteorological Authority (UNMA) - *September
 to December (SOND) 2025 Seasonal Rainfall Outlook*.

---

## 1. Executive Summary of the Domain

Uganda's climate is bimodal, characterized by two major rainfall seasons: **MAM
 (March-April-May)** and **SOND (September-October-November-December)**.

The SOND season constitutes the "second major cropping season" for most of the country.
 The success of this season determines food security and economic stability for
  the first half of the following year. The domain of this project intersects
   **Meteorology**, **Agriculture**, and **Disaster Management**.

According to the 2025 outlook, the prevailing climate drivers (including the
 ITCZ and potentially ENSO/IOD phases) are indicating a high probability of
  **"Above-Normal" (Enhanced) Rainfall** across the majority of the country.

---

## 2. Key Findings from UNMA SOND 2025 Outlook

### 🌧️ The Forecast

- **Overall Trend:** "Above-normal" rainfall is predicted for most regions.
- **Onset:** Rains are expected to establish fully by early-to-mid September in
 most districts.
- **Cessation:** Rains are expected to continue into January 2026 for several
 regions, extending the growing season but complicating the harvesting period.

### 🚜 Sector-Specific Impacts (Systems Analysis)

#### A. Agriculture & Food Security (Primary Focus)

While enhanced rainfall is generally positive for biomass production, the report
 identifies critical systemic risks:

- **Water Logging:** Excessive soil moisture leading to root rot in beans, cassava,
 and Irish potatoes.
- **Nutrient Leaching:** Heavy rains washing away fertilizers and soil nutrients,
 requiring farmers to adjust application methods.
- **Post-Harvest Losses:** High humidity and rain during the traditional harvesting
 months (Dec/Jan) will make drying cereals (maize, millet) difficult, increasing
  the risk of aflatoxins and mold.
- **Pests & Diseases:** Humid conditions favor crop pests (fall armyworm) and
 livestock diseases (ticks, tsetse flies).

#### B. Disaster Management

- **Landslides:** High-risk warning for mountainous sub-regions: **Elgon**
 (Bududa, Bulambuli) and **Kigezi/Rwenzori** (Kabale, Kisoro, Kasese).
- **Flooding:** Flash floods predicted for urban areas (Kampala, Jinja) and
 low-lying areas (Teso, Bukedi).
- **Infrastructure:** Risk of roads and bridges washing away, cutting off market
 access for farmers.

#### C. Health

- **Waterborne Diseases:** Increased risk of Cholera, Dysentery, and Bilharzia
 due to contamination of water sources by surface runoff.
- **Vector-Borne Diseases:** Stagnant water will increase Malaria vector breeding
 sites.

---

## 3. Stakeholder Analysis

<!-- markdownlint-disable MD013 -->
| Stakeholder | Interest/Needs | Capabilities & Constraints |
| :--- | :--- | :--- |
| **Smallholder Farmers** | Need to know *when* to plant and *what* to plant (short vs. long cycle crops). | **Constraint:** Lack access to complex data; rely on radio or local extension workers. |
| **District Agricultural Officers** | Need district-level forecasts to advise on fertilizer application and drainage. | **Capability:** Can interpret technical data if presented clearly. |
| **Disaster Preparedness Cmtes** | Need early warning for peak rainfall weeks to evacuate vulnerable areas. | **Constraint:** Often reactive rather than proactive due to lack of granular data. |
| **UNMA (Met Authority)** | mandate to provide weather info. | **Constraint:** Forecasts are often regional/zonal, not district-specific enough for micro-planning. |
|                          |                                  | This limits their utility for micro-planning. |
<!-- markdownlint-enable MD013 -->
---

## 4. Gap Analysis: Why Data Science?

The UNMA report provides a **probabilistic forecast at a regional level** (e.g.,
 "Western Region will see near-normal to above-normal rain").

**The Problem:**
A farmer in *Wakiso* needs more specific information than "Central Region will
 be wet." They need to know:

1. **Intensity:** Will it rain 100mm or 300mm next month?
2. **Trend:** Is the trend increasing or decreasing compared to last year?

**Our Solution:**
By utilizing **ERA5 Historical Climate Data and the Climate Hazards Data (CHIRPS)**
 (1981–2025), we aim to downscale these general trends into **granular,
  district-level predictions**. This bridges the gap between high-level
   meteorological outlooks and on-the-ground actionable decisions.

---

## 5. References & Data Sources

1. **Uganda National Meteorological Authority (UNMA):**
 *[September to December (SOND) 2025 Seasonal Rainfall Outlook](https://meteo.mwe.go.ug/media/downloads/files/September%20to%20December%20(SOND)%202025%20Seasonal%20Rainfall%20Outlook%20(1)_compressed.pdf)*.
2. **[ERA5 Reanalysis Data](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download):**
    Copernicus Climate Change Service (C3S).
3. [Climate Hazards Data (CHIRPS)](https://data.chc.ucsb.edu/products/CHIRPS-2.0/EAC_monthly/tifs/)
: Climate Hazards Center
4. **[Humanitarian Dat Exchange (HDX)](https://data.humdata.org/dataset/cod-ab-uga)**:
 Administrative boundaries for Uganda (District Shapefiles) to map our predictions.
