"""
This module defines and solves the mixed-integer portfolio optimization model.
The formulation allows the portfolio selection process to incorporate both
continuous weight allocations and binary asset inclusion decisions.

Model Structure
---------------
Decision Variables:
    x_i : continuous variable representing the portfolio weight of asset i.
    z_i : binary variable indicating whether asset i is selected in the portfolio.

Objective:
    Maximize expected portfolio return minus a risk penalty term weighted by
    a risk-aversion parameter (lambda):
        maximize   mu.T @ x - lambda * x.T @ Sigma @ x

Constraints:
    - Full investment: sum(x_i) = 1
    - Link weight and selection decisions (e.g., x_i <= z_i)
    - Optional cardinality or allocation constraints depending on model settings.

Inputs
------
mu : numpy.ndarray
    Mean return vector.
Sigma : numpy.ndarray
    Covariance matrix of asset returns.
lambda_param : float
    Risk-aversion parameter controlling the return-risk tradeoff.

Outputs
-------
solution : dict
    Dictionary containing optimal weights, selection decisions, objective value,
    and solver status.

Notes
-----
This module is solver-agnostic where possible; Pyomo is used as the modeling
interface, allowing flexibility in backend solver selection (CBC, Gurobi, etc.).
"""
