# Minimal implementations for the assignment tasks

def max_of_three(a, b, c):
	return max(a, b, c)


def distinct_elements(seq):
	out = []
	for x in seq:
		if x not in out:
			out.append(x)
	return out


def multiply_list(nums):
	prod = 1
	for n in nums:
		prod *= n
	return prod


def factorial(n):
	if n < 0:
		raise ValueError('negative')
	res = 1
	for i in range(2, n + 1):
		res *= i
	return res


def reverse_string(s):
	return s[::-1]


def is_in_range(n, start, end):
	return start <= n <= end


def print_even_numbers(lst):
	for x in lst:
		if isinstance(x, int) and x % 2 == 0:
			print(x)


def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True


def count_case(s):
	up = sum(1 for ch in s if ch.isupper())
	low = sum(1 for ch in s if ch.islower())
	return up, low
 
