import numpy as np


coefficients = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5],
], dtype=float)

constants = np.array([9, -6, 17], dtype=float)

solution_using_solve = np.linalg.solve(coefficients, constants)
solution_using_inverse = np.linalg.inv(coefficients).dot(constants)

print("Coefficient matrix:")
print(coefficients)
print()
print("Constants:")
print(constants)
print()
print("Solution using linalg.solve:")
print(solution_using_solve)
print("Solution using inverse matrix method:")
print(solution_using_inverse)
