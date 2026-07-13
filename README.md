# Interest Rate Curve Bootstrapping & Stress Testing

## Overview

This project builds an end-to-end fixed income analytics framework in Python, focusing on yield curve construction, bond pricing, and interest rate risk analysis. Starting from market quotes, the project bootstraps a zero-coupon yield curve, fits continuous term structure models, prices fixed-income securities, and evaluates portfolio sensitivity under a range of interest rate stress scenarios.

The project is developed primarily in **Jupyter Notebooks**, making each stage self-contained and easy to follow while demonstrating both the underlying financial theory and its implementation.

---

## Objectives

* Build zero-coupon yield curves from Treasury and/or SOFR market data
* Implement yield curve interpolation and curve fitting techniques
* Price zero-coupon and coupon-paying bonds
* Construct and value bond portfolios
* Apply parallel and non-parallel interest rate shocks
* Compute standard fixed income risk measures
* Produce clear visualizations of yield curves, portfolio valuation, and risk metrics

---

## Features

### Yield Curve Construction

* Load Treasury or SOFR market quotes
* Clean and validate market data
* Bootstrap discount factors
* Construct zero-coupon spot curves

### Curve Fitting

* Linear interpolation
* Cubic spline interpolation
* Nelson–Siegel model fitting
* Comparison of interpolation methods

### Bond Pricing

* Cash flow generation
* Present value pricing
* Zero-coupon bonds
* Fixed-rate coupon bonds

### Portfolio Analytics

* Portfolio valuation
* Market value aggregation
* Portfolio exposure analysis

### Interest Rate Stress Testing

* Parallel yield curve shifts
* Bear steepeners
* Bull flatteners
* Yield curve twists
* Portfolio repricing under stressed scenarios

### Risk Measures

* Macaulay Duration
* Modified Duration
* Convexity
* DV01 / PV01
* Key Rate Durations (KRDs)

---

## Project Structure

```text
interest-rate-curve/
│
├── data/
│   ├── treasury_quotes.csv
│   ├── sofr_quotes.csv
│   ├── sample_bonds.csv
│   └── portfolio.csv
│
├── notebooks/
│   ├── 01_market_data.ipynb
│   ├── 02_bootstrap_zero_curve.ipynb
│   ├── 03_curve_interpolation.ipynb
│   ├── 04_bond_pricing.ipynb
│   ├── 05_portfolio_analysis.ipynb
│   ├── 06_stress_testing.ipynb
│   ├── 07_risk_measures.ipynb
│   └── 08_final_case_study.ipynb
│
├── figures/
├── README.md
└── requirements.txt
```

---

## Workflow

1. Load and clean market data.
2. Bootstrap a zero-coupon yield curve from observed market quotes.
3. Fit continuous yield curves using multiple interpolation techniques.
4. Price individual bonds using discount factors.
5. Construct and value a bond portfolio.
6. Apply interest rate stress scenarios.
7. Reprice the portfolio under each scenario.
8. Calculate portfolio risk measures and summarize results.

---

## Technologies

* Python
* Jupyter Notebook
* NumPy
* Pandas
* SciPy
* Matplotlib
* Plotly (optional)

---

## Learning Outcomes

This project demonstrates practical skills in:

* Fixed Income Analytics
* Yield Curve Construction
* Financial Engineering
* Numerical Methods
* Optimization
* Risk Management
* Scientific Computing with Python
* Financial Data Visualization

---

## Future Improvements

Potential extensions include:

* SOFR swap curve bootstrapping
* Svensson yield curve model
* Historical yield curve replay
* Principal Component Analysis (PCA) of yield curve movements
* Value-at-Risk (VaR)
* Hedging with Treasury futures
* Interactive Streamlit dashboard

---

## References

* John C. Hull — *Options, Futures, and Other Derivatives*
* Frank J. Fabozzi — *Fixed Income Analysis*
* Tuckman & Serrat — *Fixed Income Securities*
* U.S. Department of the Treasury
* Federal Reserve Bank of New York (SOFR)

---

## License

This project is intended for educational and portfolio purposes. Feel free to use, modify, and extend the code with appropriate attribution.
