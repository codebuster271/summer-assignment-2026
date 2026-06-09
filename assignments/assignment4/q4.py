def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


print(factorial(5))