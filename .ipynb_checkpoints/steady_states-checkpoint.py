import numpy as np
from scipy.optimize import fsolve

import numpy as np
from scipy.optimize import fsolve

def find_steady_states(system_func, num_vars, num_samples=500, tol=1e-8, domain=None):
    """
    Search for unique steady states of an n-dimensional dynamical system
    by sampling random initial conditions and solving f(X) = 0.

    Parameters:
    -----------
    system_func : callable
        A function that takes a list or array of variables [x1, x2, ..., xn]
        and returns the list of derivatives [dx1/dt, dx2/dt, ..., dxn/dt].

    num_vars : int
        The number of variables (dimensions) in the system.

    num_samples : int, optional
        Number of random initial guesses to try. Default is 500.

    tol : float, optional
        Tolerance for distinguishing unique solutions. Default is 1e-8.

    domain : list of tuple(float, float), optional
        Bounds for each variable as [(min1, max1), (min2, max2), ...].
        If not provided, defaults to [(0, 1)] for all variables.

    Returns:
    --------
    roots : list of np.ndarray
        A list of unique steady-state vectors [x1_ss, ..., xn_ss]
        that satisfy the condition f(X) ≈ 0 within the specified domain.
    """
    # Default domain: unit cube if none is specified
    if domain is None:
        domain = [(0, 1)] * num_vars

    roots = []  # Store unique steady-state solutions

    # Generate random initial guesses within the domain bounds
    rng = np.random.default_rng()
    guesses = np.array([
        [rng.uniform(low, high) for (low, high) in domain]
        for _ in range(num_samples)
    ])

    # Loop through each initial guess
    for guess in guesses:
        sol, info, ier, _ = fsolve(system_func, guess, full_output=True)

        # If solver fails to converge, skip this guess
        if ier != 1:
            continue

        # Check if the solution lies within domain bounds
        within_bounds = all(low <= val <= high for val, (low, high) in zip(sol, domain))
        if not within_bounds:
            continue

        # Skip if this solution is too close to one already found
        already_found = any(np.allclose(sol, existing, atol=tol) for existing in roots)
        if already_found:
            continue

        # Store unique valid steady state
        roots.append(sol)

    return roots
