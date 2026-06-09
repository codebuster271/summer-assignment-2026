def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply_list([2, 3, 4]))