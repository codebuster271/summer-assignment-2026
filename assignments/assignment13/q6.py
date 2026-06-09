"""Assignment 13 - Question 6."""

import numpy as np


def main():
    coefficients = np.array(
        [
            [1, -2, 3],
            [-1, 3, -1],
            [2, -5, 5],
        ],
        dtype=float,
    )
    constants = np.array([9, -6, 17], dtype=float)

    solution_using_solve = np.linalg.solve(coefficients, constants)
    solution_using_inverse = np.linalg.inv(coefficients).dot(constants)

    print("System of equations:")
    print("x - 2y + 3z = 9")
    print("-x + 3y - z = -6")
    print("2x - 5y + 5z = 17")
    print()
    print("Solution using numpy.linalg.solve():")
    print(solution_using_solve)
    print("Solution using inverse matrix method:")
    print(solution_using_inverse)
    print()
    print("Residual check:")
    print(coefficients.dot(solution_using_solve) - constants)


if __name__ == "__main__":
    main()
