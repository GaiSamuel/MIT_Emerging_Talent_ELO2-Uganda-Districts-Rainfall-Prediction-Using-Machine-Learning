# 📈 Data Analysis & Modeling

**Goal:** This folder contains the machine learning pipeline used to predict
 district-level rainfall in Uganda for the 2025–2026 period.

## 1. Analysis Strategy

Our approach balances complexity with interpretability, using a tree-based
 ensemble method that handles non-linear climate interactions well.

### 🧠 The Model: Random Forest Regressor

We selected **Random Forest** over simpler linear models because:

- **Non-Linearity:** Rainfall drivers (like El Niño or pressure systems) don't
 have simple linear relationships with precipitation.
- **Interaction:** It captures complex interactions between variables (e.g., how
 High Temperature + Low Wind = Convection Rain).
- **Robustness:** It is less sensitive to outliers than Neural Networks, which is
 crucial for noisy weather data.

### 🔄 Data Batching & Validation Strategy

*How we ensured the model predicts the future, not the past.*

1. **Training Batch (The Past):**
    - **Period:** Jan 1981 – Dec 2018 (38 years)
    - **Purpose:** The model learns long-term climate trends, seasonal cycles
   (MAM/SON), and physical relationships between variables (e.g., how temperature
    affects rainfall).
    - **Size:** ~85% of the total dataset.

2. **Validation Batch (The "Future"):**
    - **Period:** Jan 2019 – Oct 2025 (7 years)
    - **Purpose:** We test the model on this unseen "future" data to simulate
   real-world forecasting. If the model can accurately predict the 2020 floods
    using only data from before 2019, we know it is robust.
    - **Size:** ~15% of the total dataset.

**Why this matters:**
This approach mimics the real-world constraint where we only have data up to
 Oct 2025 and need to predict Nov 2025 onwards. It prevents **Data Leakage** and
  ensures our accuracy metrics (RMSE) reflect true predictive power.

### 🛠 Feature Engineering

To turn raw dates into learnable patterns, we created three categories of features:

1. **Temporal:** `Year` (Trend), `Month` (Seasonality), and One-Hot Encoded
 `Seasons` (MAM, SON, etc.).
2. **Autoregressive (Lags):** `rain_lag_1` (Last month's rain) and `rain_lag_3`.
 *Hypothesis: Rainfall is "sticky"; wet soil leads to more rain.*
3. **Moving Averages:** `rainfall_rolling_mean_3` (Quarterly trend). *Hypothesis:
 Smooths out daily noise to show the "wetness state" of the region.*

> **⚠️ Leakage Prevention:** All rolling means were calculated using `.shift(1)`
to ensure the model never sees the target month's data when making a prediction.

---

## 2. Notebooks & Scripts

<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD033 -->
| File | Description |
| :--- | :--- |
| **[`data_analysis.ipynb`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/4_data_analysis/data_analysis.ipynb)** | **The Core Pipeline.** <br>1. Loads clean data.<br>2. Generates Lag/Rolling features.<br>3. Splits data by Time (Train < 2019).<br>4. Trains the Random Forest.<br>5. Generates the 14-month recursive forecast. |
| *[`raw_data_exploration.ipynb`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/3_data_exploration/raw_data_exploration.ipynb)* | *Pre-analysis visualization of historical trends (See Exploration folder).* |
| *[`predicted_data_exploration.ipynb`](https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning/blob/main/3_data_exploration/predicted_data_exploration.ipynb)*| *Post-modeling validation. Visualizes the 14-month forecast to confirm seasonality (bimodal pattern), spatial distribution (wettest vs. driest districts), and regional consistency (See Exploration folder).*                             |
<!-- markdownlint-enable MD033 -->
<!-- markdownlint-enable MD013 -->
---

## 3. Model Performance (Results)

We validated the model using a **Time-Based Split**, training on 1981–2018 and
 testing on 2019–2025. This ensures we are testing the model's ability to predict
  the *future*, not just fill in gaps.

### Key Metrics

<!-- markdownlint-disable MD013 -->
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **RMSE** | **~43.2 mm** | On average, our prediction is off by 43mm. |
| **Baseline RMSE** | **~68.1 mm** | If we just guessed the "average", we'd be off by 68mm. |
| **Improvement** | **+36%** | Our model is 36% more accurate than random guessing. |
| **R² Score** | **~0.60** | The model explains 60% of the variance in rainfall. |
| **Pseudo-Accuracy**| **~75%** | Predictions are generally within 25% of the true value. |
<!-- markdownlint-enable MD013 -->

---

## 4. Forecasting Strategy (The Future)

Since we don't have future weather data to feed the model, we used a
 **Recursive Forecasting** strategy for Nov 2025 – Dec 2026.

1. **Step 1:** Predict Month $t$ using known history.
2. **Step 2:** Use the *prediction* from Month $t$ as the "Lag 1" input for
 Month $t+1$.
3. **Step 3:** Repeat for 14 months.
4. **Static Features:** For atmospheric drivers (Temp, Wind, Pressure), we used
 **Climatological Means** (historical monthly averages) as proxies for the future
  state.

### Outputs

- **Model File:** [`uganda_rainfall_forecast_model.pkl`](https://drive.google.com/drive/folders/1wB9zG6Q8cKY9EpyBWGnr2yRmjLtFkYrU)
 (Saved Random Forest object).
- **Forecast CSV:** `uganda_rainfall_forecasts_2025_2026.csv` (Final predictions).

---

## 🚀 How to Replicate

1. Ensure the clean dataset exists in `1_datasets/clean_data` folder.
2. Open `data_analysis.ipynb`.
3. Run all cells.
4. The script will:
    - Train the model.
    - Print validation metrics.
    - Save the new forecast file to the `1_datasets/clean_data` folder.
