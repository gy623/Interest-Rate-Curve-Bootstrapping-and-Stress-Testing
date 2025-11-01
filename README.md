# Mixed-Integer Portfolio Optimization Project

This project develops and evaluates a portfolio optimization framework that uses
mixed-integer programming (MIP) to enforce realistic trading and portfolio construction
constraints. The objective is to compare integer-constrained portfolios with standard
continuous mean-variance portfolios and measure performance differences in backtests.

## Objectives
- Construct and solve mixed-integer portfolio optimization problems.
- Incorporate cardinality, minimum position size, turnover, and transaction cost constraints.
- Integrate the optimizer into a historical backtesting workflow.
- Evaluate realized risk-adjusted performance and implementation costs.

## Project Structure

quant-mip-portfolio/
├─ data/              # Market data (not stored in repo if large)
├─ notebooks/         # Exploratory and results notebooks
├─ src/               # Source code (data loading, optimizer, backtesting)
├─ reports/           # Final report, slides, derivations
├─ requirements.txt   # Python dependencies
└─ README.md          # Project overview

## Planned Deliverables
- Reproducible Jupyter notebooks demonstrating methodology and results.
- Modular Python codebase for data handling, model construction, and backtesting.
- Report summarizing findings, assumptions, and quantitative performance metrics.

