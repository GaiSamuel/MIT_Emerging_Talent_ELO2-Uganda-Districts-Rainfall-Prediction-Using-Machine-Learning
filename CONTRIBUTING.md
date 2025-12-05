# Contributing to the Uganda Rainfall Prediction Project

Thank you for your interest in contributing to our project! We welcome contributions
 from data scientists, developers, and domain experts to help improve our rainfall
  prediction model and communication tools.

This document outlines the guidelines for contributing to ensure a smooth and
 collaborative process.

---

## 🤝 How You Can Contribute

We are looking for help in the following areas:

- **Data Collection:** Regarding the excluded 15 districts due to missing data,
 if you have access
 to reliable sources for filling these gaps, please let us know.
- **Feature Engineering:** Suggesting or implementing new features that could
 better capture rainfall patterns.
- **Modeling:** Experimenting with different machine learning algorithms (e.g.,
 XGBoost, LSTM) to beat our current baseline.
- **Visualization:** Improving the interactive dashboard or creating new static
 visualizations for reports.
- **Documentation:** Fixing typos, clarifying complex sections, or translating
 insights into local languages.

---

## 🛠 Development Setup

To get started with the project locally:

### 1. Fork the Repository

Click the **"Fork"** button at the top right of this page.

### 2. Clone Your Fork

Run the following command in your terminal:

```bash
git clone https://github.com/GaiSamuel/MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning.git
cd MIT_Emerging_Talent_ELO2-Uganda-Districts-Rainfall-Prediction-Using-Machine-Learning
```

### 3. Set Up Environment

- Ensure you have Python 3.8+ installed.
- Install the required packages:

```bash
pip install pandas xarray glob numpy matplotlib seaborn scikit-learn joblib
 geopandas rasterstats
```

### 4. Explore the Data

- The clean dataset is located at: 1_datasets/clean_data/`uganda_monthly_rainfall_and_climate_variables_1981_2025.csv`

- Important: Do not modify files in `raw_data/.`

---

### 📜 Submission Guidelines

**Reporting Bugs:**  

If you find a bug in the code or an error in the data, please open an Issue describing:

- What you expected to happen.
- What actually happened.
- Steps to reproduce the error.

**Suggesting Enhancements:**

If you have an idea for a new feature or analysis:

1. Open an Issue with the tag enhancement.
2. Describe your idea and why it would be valuable.
3. Wait for feedback before starting significant work.

### Pull Requests (PRs)

**Create a Branch**: Always work on a new branch for your changes.

```bash
git checkout -b feature/your-feature-name
```

**Follow Coding Standards**:

- Use clear variable names.
- Comment your code, especially complex logic.
- Ensure notebooks are cleared of output before committing (unless the output
  is the point).

**Test Your Changes**: Verify that your code runs without errors and produces
 expected results.

**Submit PR**: Push your branch and open a Pull Request against the main branch.

- Reference any relevant Issues.
- Provide a clear description of your changes.

### 📄 License

By contributing, you agree that your contributions will be licensed under the
 project's MIT License.

### 💬 Community

If you have questions, feel free to reach out to the maintainers:

Gai Samuel: [GitHub](https://github.com/GaiSamuel) | [LinkedIn](https://linkedin.com/in/samuel-gai)

Anyak Abraham: [GitHub](https://github.com/Anyak7) | [LinkedIn](https://www.linkedin.com/in/anyak-abraham-b9721a315/)

Thank you for helping us support Ugandan farmers with better climate data! 🌍🌧️
