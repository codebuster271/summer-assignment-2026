def print_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(even_numbers)


print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8])