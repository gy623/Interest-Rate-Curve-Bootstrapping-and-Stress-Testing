# Interest Rate Curve Bootstrapping and Fixed Income Risk Analytics

## Overview

This project builds a complete fixed-income analytics framework for constructing yield curves, pricing bonds, and measuring interest rate risk.

The objective is to replicate the workflow used in fixed-income trading and risk management:

1. Construct a zero-coupon yield curve from market instruments
2. Bootstrap discount factors from Treasury bills and notes
3. Interpolate the curve using spline and parametric methods
4. Price fixed-income securities
5. Perform yield curve stress testing
6. Quantify portfolio interest rate risk using duration, convexity, DV01, and key rate durations

The project is implemented entirely in Python using Jupyter notebooks, with each notebook representing one stage of the fixed-income pricing pipeline.

---

# Project Structure
```text
interest-rate-curve-boostrapping-and-stress-testing/
│
├── data/
│   ├── treasury_yields.csv
│   ├── bootstrapped_treasury_bills.csv
│   ├── clean_treasury_curve.csv
│   ├── continuous_zero_curve.csv
│   ├── zero_curve.csv
│   └── sample_portfolio.csv
│
├── notebooks/
│   ├── 01_market_data.ipynb
│   ├── 02_bootstrap_zero_curve.ipynb
│   ├── 03_curve_interpolation.ipynb
│   ├── 04_bond_pricing.ipynb
│   ├── 05_portfolio_analysis.ipynb
│   └── 06_stress_testing.ipynb
│
└── README.md
```


---

# Stage 1 — Market Data and Curve Construction

## Objective

Prepare Treasury market data and construct the initial set of fixed-income instruments used for bootstrapping.

The dataset contains:

- Treasury bills (short-term instruments)
- Treasury notes (coupon-bearing securities)
- Maturity dates
- Coupon rates
- Market yields

Treasury bills are treated as zero-coupon instruments, while Treasury notes require bootstrapping to extract implied discount factors.

---

# Stage 2 — Yield Curve Bootstrapping

## Objective

Construct zero-coupon discount factors from observed Treasury prices.

The fundamental pricing relationship is:

$$
P = \sum_{i=1}^{n} CF_i DF_i
$$

where:

- $P$ = observed bond price
- $CF_i$ = cash flow at time $i$
- $DF_i$ = discount factor

---

## Treasury Bills

Bills are assumed to be zero-coupon securities:

$$
P = \frac{F}{(1+r)^T}
$$

Therefore:

$$
DF(T)=\frac{P}{F}
$$

where:

- $F$ = face value
- $r$ = quoted yield
- $T$ = maturity

---

## Treasury Notes

For coupon-bearing bonds, discount factors are solved iteratively.

For a bond with maturity $T$:

$$
P =
\sum_{i=1}^{n-1} C_iDF_i
+
(F+C_n)DF_n
$$

Rearranging:

$$
DF_n=
\frac{
P-\sum_{i=1}^{n-1}C_iDF_i
}
{
F+C_n
}
$$

This process is repeated sequentially for increasing maturities.

The output is a complete set of zero-coupon discount factors.

---

# Stage 3 — Yield Curve Construction and Interpolation

## Objective

Convert discrete discount factors into a continuous zero-coupon yield curve.

The spot rate is calculated as:

\[
r(T)=DF(T)^{-\frac{1}{T}}-1
\]

where:

- $DF(T)$ = discount factor
- $T$ = maturity

The resulting curve is interpolated using:

### Cubic Spline Interpolation

A smooth curve is generated between observed maturities:

$$
r(T)=Spline(T)
$$

Advantages:

- Smooth derivatives
- Flexible shape
- Good for pricing applications

---

### Nelson-Siegel Model

A parametric representation of the yield curve:

$$
r(T)
=
\beta_0
+
\beta_1
\frac{1-e^{-T/\tau}}{T/\tau}
+
\beta_2
\left(
\frac{1-e^{-T/\tau}}{T/\tau}
-e^{-T/\tau}
\right)
$$

where:

- $\beta_0$ controls long-term level
- $\beta_1$ controls slope
- $\beta_2$ controls curvature
- $\tau$ controls decay speed

---

# Stage 4 — Bond Pricing Engine

## Objective

Develop a general bond pricing framework using the bootstrapped zero curve.

The bond price is:

$$
P=
\sum_{i=1}^{n}
CF_iDF_i
$$

where:

$$
DF_i=\frac{1}{(1+r_i)^{t_i}}
$$

The pricing engine supports:

- Coupon bonds
- Different maturities
- Different coupon frequencies
- Arbitrary yield curves

---

# Stage 5 — Portfolio Valuation and Stress Testing

## Objective

Extend individual bond pricing to a portfolio level and analyse interest rate scenarios.

Portfolio value:

$$
V=
\sum_i P_iN_i
$$

where:

- $P_i$ = bond price
- $N_i$ = face value

---

## Yield Curve Shocks

The project implements:

### Parallel Shift

All rates move by the same amount:

$$
r(T)\rightarrow r(T)+\Delta r
$$


### Steepener

Long-term rates increase more than short-term rates.


### Flattener

Short-term rates increase more than long-term rates.


### Twist

Short and long maturities move in opposite directions.

---

Portfolio values are recalculated under each scenario:

$$
\Delta V=V_{shock}-V_{base}
$$

allowing portfolio profit and loss to be analysed.

---

# Stage 6 — Fixed Income Risk Measures

## Objective

Quantify interest rate sensitivity using standard fixed-income risk metrics.

---

# Duration

## Macaulay Duration

Measures the weighted average time of receiving a bond's cash flows:

$$
D_M
=
\frac{
\sum_i t_iPV(CF_i)
}
{P}
$$

where:

- $t_i$ = payment time
- $PV(CF_i)$ = discounted cash flow
- $P$ = bond price

---

## Effective Duration

Since the project prices using a full spot curve, duration is calculated through curve bumping:

$$
D_{eff}
=
\frac{
P_{-}-P_{+}
}
{
2P_0\Delta y
}
$$

where:

- $P_-$ = price after a downward rate shift
- $P_+$ = price after an upward rate shift
- $\Delta y$ = yield change

This measures the percentage price sensitivity to interest rate changes.

---

# Convexity

Convexity captures the curvature of the price-yield relationship.

Effective convexity is calculated numerically:

$$
C
=
\frac{
P_{+}+P_{-}-2P_0
}
{
P_0(\Delta y)^2
}
$$

A higher convexity indicates:

- Larger gains when rates fall
- Smaller losses when rates rise

---

# DV01 / PV01

DV01 measures the dollar price change caused by a one basis point move:

$$
DV01=P_0-P_{+1bp}
$$

It is widely used by fixed-income traders to measure interest rate exposure.

---

# Key Rate Duration

Effective duration assumes a parallel curve shift.

Key Rate Duration measures sensitivity to individual maturities.

For maturity $k$:

$$
KRD_k
=
\frac{
V_0-V_k
}
{
V_0\Delta y
}
$$

where only the $k$-year point on the yield curve is shifted.

This identifies whether a portfolio is primarily exposed to:

- Short-term rates
- Medium-term rates
- Long-term rates

---

# Duration Approximation

The project compares exact repricing against duration-based approximations.

First-order approximation:

$$
\frac{\Delta P}{P}
\approx
-D\Delta y
$$

Including convexity:

$$
\frac{\Delta P}{P}
\approx
-D\Delta y
+
\frac12C(\Delta y)^2
$$

The comparison demonstrates why convexity improves accuracy for larger interest rate movements.

---

# Final Outputs

The project produces:

## Yield Curve Analytics

- Bootstrapped discount factors
- Zero-coupon curve
- Cubic spline interpolation
- Nelson-Siegel fitted curve

## Pricing Analytics

- Bond prices
- Portfolio valuation
- Scenario-based repricing

## Risk Analytics

- Effective duration
- Effective convexity
- DV01
- Key rate durations
- Duration-convexity approximation

---

# Key Concepts Demonstrated

This project applies core quantitative finance concepts:

- Discount factor bootstrapping
- Fixed-income pricing
- Yield curve modelling
- Numerical interpolation
- Scenario analysis
- Interest rate risk measurement

The final framework provides a simplified implementation of the fixed-income analytics workflow used by quantitative researchers, traders, and risk managers.