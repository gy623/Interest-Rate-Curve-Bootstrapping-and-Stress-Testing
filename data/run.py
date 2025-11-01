"""
Execute the mixed-integer portfolio selection pipeline.

This script coordinates the full workflow:
    1. Load and preprocess financial data.
    2. Compute expected returns and covariance matrix.
    3. Construct and solve the mixed-integer optimization model.
    4. Report the optimal portfolio allocation and model performance metrics.

Execution
---------
Run from the project root using:

    python src/run.py

Outputs
-------
Printed model results or saved report files depending on configuration.

Notes
-----
This file is intentionally lightweight. All domain logic is delegated to
`data_loader.py` and `mip_model.py`, ensuring the execution pipeline remains
modular and maintainable.
"""


