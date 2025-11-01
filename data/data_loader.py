"""
This module provides functions for loading and preprocessing financial time-series
data for use in the mixed-integer portfolio optimisation model.

Responsibilities
----------------
- Import historical asset price data from local storage or external data sources.
- Convert price series into return series (log returns or arithmetic returns).
- Compute the expected returns vector (mu) and the covariance matrix (Sigma) used
  in the optimisation objective.

Outputs
-------
mu : numpy.ndarray
    Mean return vector for each asset.
cov : numpy.ndarray
    Covariance matrix representing asset return variances and correlations.

Notes
-----
This module is intentionally isolated from optimisation logic to maintain a
clear separation of concerns between data processing and model formulation.
"""
