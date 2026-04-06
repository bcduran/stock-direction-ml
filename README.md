# DS540 Machine Learning Project  
## Predicting Next-Day Stock Price Direction with Machine Learning Models

This project investigates the binary classification problem of forecasting whether a stock’s closing price will move **up (1)** or **down (0)** on the next trading day.

Using **CRSP-based daily stock data**, technical indicators, and a structured feature engineering pipeline, the project compares multiple machine learning and deep learning approaches for next-day stock direction prediction.

This work was developed as part of **DS540 – Machine Learning with Python**.

---

## Project Objective

The main objective is to predict the **next-day price direction** of selected NYSE-listed stocks using engineered technical indicators and compare the performance of:

- **Boosting models**: XGBoost and CatBoost  
- **Recurrent neural networks**: LSTM (including deeper and bidirectional variants)  
- **Temporal models**: Temporal Convolutional Networks (TCN)

---

## Dataset

- **Source**: CRSP-derived daily stock data  
- **Period**: 2020–2024 (with focused modelling on 2023–2024 subsets in some experiments)  
- **Universe**:
  - Core subset: **BA, GM, BAC, C, T**
  - Extended cross-section: **1,800+ equities** in broader experiments

### Raw Variables
The original dataset includes fields such as:

- `date`
- `ticker`
- `prc`
- `ret`
- `vol`
- `shrout`
- `openprc`
- `bidlo`
- `askhi`
- `shrcd`
- `exchcd`

> Note: Due to data licensing and access restrictions, raw CRSP data is **not included** in this repository.

---

## Target Definition

The target is defined as a binary classification variable:

- **1 (UP)** if `Close_{t+1} > Close_t`
- **0 (DOWN)** otherwise

Equivalent implementation in the pipeline:
- `target_ret = next_day_return`
- `target_class = 1 if target_ret > 0 else 0`

---

## Feature Engineering

The following technical and market-based features were engineered:

- **Market capitalization**
- **5-day momentum**
- **20-day moving average (SMA)**
- **30-day realized volatility**
- **RSI (14)**
- **MACD**
- **MACD signal**
- **Bollinger Bands (upper/lower)**
- Additional technical ratios and transformations used in modelling notebooks

### Feature Selection Pipeline

A structured feature reduction process was applied:

1. **Variance Thresholding**  
   Removed low-variance features with limited predictive value.

2. **Correlation Filtering**  
   Removed highly correlated features (Pearson correlation > 0.90) to reduce multicollinearity.

3. **Recursive Feature Elimination (RFE)**  
   Used a tree-based estimator to rank and retain the most informative predictors.

After filtering, the final subset contained approximately **8–9 key features**, depending on the model family.

---

## Modeling Approaches

### 1. XGBoost
- Baseline gradient-boosted tree classifier
- Time-based train/test split
- Hyperparameter tuning performed with **Optuna**
- Evaluated with ROC AUC, accuracy, F1 score, and confusion matrix

### 2. CatBoost
- Trained as a cross-sectional model across multiple tickers
- Included `ticker_code` as a categorical feature
- Used for feature importance and **SHAP-based explainability**

### 3. LSTM
- Ticker-specific sequence models
- Built to capture temporal dependencies in stock price movement
- Included:
  - stacked LSTM
  - bidirectional LSTM
  - regularization via dropout and batch normalization

### 4. Temporal Convolutional Network (TCN)
- Dilated 1D convolutions
- Designed to model long-range dependencies efficiently
- Compared against recurrent architectures

---

## Project Structure

```text
stock-direction-ml/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── data/
│   └── README.md
│
├── notebooks/
│   ├── crsp_stock_forecasting_updated.ipynb
│   ├── modelling_xgboost.ipynb
│   └── modelling_lstm.ipynb
│
├── src/
    ├── data_cleaning.py
    ├── feature_engineering.py
    ├── baseline_check.py
    └── compustat_features.py
