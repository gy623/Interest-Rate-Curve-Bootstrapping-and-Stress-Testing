# Interest Rate Curve Boostrapping and Stress Testing

> A professional-grade fixed income risk analytics pipeline for constructing
> zero-coupon yield curves from SOFR / Treasury market data, performing
> curve interpolation, applying interest rate stress scenarios, and computing
> full portfolio risk metrics including Duration, Convexity, and Key Rate Durations (KRDs).

---

## 🧭 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Pipeline Architecture](#pipeline-architecture)
- [Modules](#modules)
  - [Data Loader](#1-data-loader)
  - [Bootstrapper](#2-bootstrapper)
  - [Interpolator](#3-interpolator)
  - [Stress Engine](#4-stress-engine)
  - [Bond Pricer](#5-bond-pricer)
  - [Risk Metrics](#6-risk-metrics)
  - [Portfolio Runner](#7-portfolio-stress-runner)
- [Stress Scenarios](#stress-scenarios)
- [Risk Metrics Reference](#risk-metrics-reference)
- [Configuration](#configuration)
- [Running the Notebooks](#running-the-notebooks)
- [Testing](#testing)
- [Validation](#validation)
- [Roadmap](#roadmap)
- [References](#references)
- [License](#license)

---

## Overview

This project implements a **full fixed income risk analytics pipeline** used in
institutional trading desks, risk management teams, and quantitative research.

Starting from raw market instruments — US Treasury CMT rates, SOFR deposit
rates, SOFR futures, and interest rate swaps — the pipeline:

1. **Bootstraps** a zero-coupon discount factor curve
2. **Interpolates** the curve continuously using Cubic Spline or Nelson-Siegel
3. **Applies** parallel and non-parallel interest rate shocks
4. **Reprices** bond portfolios under each stressed curve
5. **Computes** Modified Duration, Convexity, and Key Rate Durations (KRDs)
6. **Produces** a full P&L attribution table across all bonds and scenarios

This is the same analytical framework used by fixed income desks at major
financial institutions for regulatory stress testing (FRTB, Basel III),
portfolio risk management, and hedging strategy.

---

## Features

- ✅ **Live data ingestion** from FRED API (US Treasury CMT rates)
- ✅ **Multi-instrument bootstrapping** — deposits, SOFR futures, and swaps
- ✅ **Two interpolation methods** — Cubic Spline and Nelson-Siegel parametric fit
- ✅ **8 pre-built stress scenarios** — parallel, steepener, flattener, twist
- ✅ **Full bond pricing engine** — DCF using zero curve discount factors
- ✅ **Modified Duration & Convexity** — analytical and numerical computation
- ✅ **Key Rate Duration (KRD) ladder** — 14-bucket sensitivity grid
- ✅ **Portfolio-level P&L matrix** — bonds × scenarios
- ✅ **Built-in validation** — KRD sum ≈ Modified Duration check
- ✅ **Interactive Jupyter notebooks** — step-by-step walkthrough
- ✅ **Extensible design** — plug in Bloomberg/Refinitiv data, QuantLib, PCA shocks

---

## Project Structure