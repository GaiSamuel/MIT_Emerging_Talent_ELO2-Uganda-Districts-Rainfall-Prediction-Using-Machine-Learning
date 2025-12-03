# 🔍 Exploratory Data Analysis

**Goal:** This folder contains the exploratory data analysis (EDA) notebooks
 used to understand both our historical training data and our final model
  predictions. These scripts focus on visualizing trends, distributions, and
   spatial patterns without running complex inference.

## 1. Historical Data Analysis

- **File:** [`raw_data_exploration.ipynb`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/3_data_exploration/raw_data_exploration.ipynb)
- **Dataset:** `uganda_monthly_rainfall_and_climate_variables_1981_2025.csv`
 (44 Years of History)

### Key Analyses Performed

1. **Distributions:** Checked for normality in variables. Found that rainfall
 is right-skewed (Gamma distribution), while temperature is normally distributed.
2. **Correlation Matrix:** Identified the relationship between rainfall and
 drivers like Temperature, Pressure, and Wind Components.
3. **Seasonality:** Visualized the annual cycle to confirm Uganda's bimodal
 rainfall pattern (MAM and SON seasons).
4. **Spatial Analysis:** Ranked the wettest vs. driest districts and compared
 rainfall variability across regions.
5. **Time Series Decomposition:** Used Rolling Averages and Anomaly detection to
 separate long-term trends from seasonal noise.
6. **Statistical Checks:** Used ACF/PACF plots to confirm significant
 autocorrelation (history predicts the future), verifying the data is suitable
  for time-series modeling.

### 💡 Interpretation of Results

- **Seasonality:** The data confirms two distinct rainy seasons: **Long Rains
 (March-May)** and **Short Rains (September-November)**.
- **Geography:**
  - **Wettest:** The Lake Victoria Basin (e.g., Kalangala) is significantly
 wetter (>150mm/mo) than the rest of the country.
  - **Driest:** The Karamoja region (e.g., Kotido, Moroto) and the Western Rift
 (Buliisa) act as semi-arid outliers.
- **Climate Drivers:** Rainfall shows a positive correlation with **Cloud Cover**
 and significant autocorrelation with **Lag-1 Rainfall** (last month's rain),
  which became a key feature in our model.

---

## 2. Forecast Output Analysis

- **File:** [`predicted_data_exploration.ipynb`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/3_data_exploration/predicted_data_exploration.ipynb)
- **Dataset:** `uganda_rainfall_forecasts_2025_2026.csv` (14-Month Forecast)

### Main Analyses Performed

1. **Temporal Trends:** Plotted the national average rainfall from Nov 2025 to
 Dec 2026 to verify that the model reproduces the expected seasonal cycle.
2. **Spatial Extremes:** Identified which districts are predicted to receive
 the most and least rain in the coming year.
3. **Regional Breakdown:** Visualized how the forecast differs between Central,
 Northern, Eastern, and Western regions.
4. **Distribution Check:** Validated that the predicted values fall within a
 realistic range (mostly 50-200mm) and follow a similar distribution to historical
  data.

### 💡 Interpreting Results

- **Model Validity:** The forecast successfully captures the **bimodal pattern**,
 predicting a peak in April 2026 and another in October 2026. This suggests the
  model has learned the underlying physics of the region.
- **Regional Divergence:**
  - **Northern Region:** Shows a "Unimodal" tendency (one long rainy season) in
 the forecast, which aligns with the climatology of Northern Uganda.
  - **Central/Western:** Clearly shows the "Double Peak" pattern.
- **Risk Identification:** The forecast predicts total rainfall <1000mm for
 districts like **Ntoroko** and **Buliisa**, highlighting potential drought
  risks for 2026. Conversely, **Kalangala** exceeds 2500mm, posing flood risks.

**[district_graphs.ipynb:](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/3_data_exploration/district_graphs.ipynb)**  

- Batch Generation of District Forecast Plots To facilitate localized analysis,
 this notebook contains a script that automates the visualization of rainfall
  trends for all districts in the dataset.
  - Process: Iterates through unique districts in the 2025-2026 forecast dataset.
  - Visualization: Uses `Seaborn` to generate line graphs showing predicted
   rainfall (mm) over time.
  - Output: Automatically exports and saves high-resolution PNG images to the
   `graphs/district_plots/` folder with standardized filenames (e.g., `Mukono_predicted_rainfall.png`).

---

## 🚀 How to Run

To replicate these insights, ensure your environment has `seaborn`, `matplotlib`,
 and `statsmodels` installed, then run:

```bash
jupyter notebook raw_data_exploration.ipynb
jupyter notebook predicted_data_exploration.ipynb
jupyter notebook district_graphs.ipynb
```
