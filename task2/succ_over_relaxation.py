import numpy as np
from scipy import linalg

from matrix_init import init_matrix_, m_get_error_matrix_norm,\
    builPlot

SIGMA = 1e-8


def init_value(n=99):
    return [i + 1 for i in range(n + 1)]


def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    """
    This is an implementation of the pseudo-code provided in the Wikipedia article.
    Arguments:
        A: nxn numpy matrix.
        b: n dimensional numpy vector.
        omega: relaxation factor.
        initial_guess: An initial solution guess for the solver to start with.
        convergence_criteria: The maximum discrepancy acceptable to regard the current solution as fitting.
    Returns:
        phi: solution vector of dimension n.
    """
    step = 0
    phi = initial_guess[:]
    residual = m_get_error_matrix_norm(A, initial_guess, b)

    all_errors_list = []

    while residual > convergence_criteria:
        all_errors_list.append(m_get_error_matrix_norm(A, phi, b))

        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i, j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
        residual = linalg.norm(A @ phi - b)
        step += 1
        print("Step {} Residual: {:10.6g}".format(step, residual))

    builPlot(all_errors_list, 'relaxation')

    return phi


# An example case that mirrors the one in the Wikipedia article
omega = 0.5  # Relaxation factor

A = np.array(init_matrix_())
b = np.array(init_value())

initial_guess = np.zeros_like(b, np.float_)

phi = sor_solver(A, b, omega, initial_guess, SIGMA)

print(f"Solution: {phi}")
print(f'error value:{m_get_error_matrix_norm(A, phi, b)}')
