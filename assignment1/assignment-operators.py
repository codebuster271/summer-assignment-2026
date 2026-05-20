# Assignment Operators Practice
# Assignment operators are used to assign values to variables

# Basic assignment
x = 10
print(f"Initial x: {x}")

# += (Add and assign)
x += 5  # x = x + 5
print(f"After += 5: {x}")

# -= (Subtract and assign)
x -= 3  # x = x - 3
print(f"After -= 3: {x}")

# *= (Multiply and assign)
x *= 2  # x = x * 2
print(f"After *= 2: {x}")

# /= (Divide and assign)
x /= 4  # x = x / 4
print(f"After /= 4: {x}")

# //= (Floor divide and assign)
x //= 2  # x = x // 2
print(f"After //= 2: {x}")

# %= (Modulus and assign)
x %= 5  # x = x % 5
print(f"After %= 5: {x}")

# **= (Exponent and assign)
x **= 2  # x = x ** 2
print(f"After **= 2: {x}")

# &= (Bitwise AND and assign)
y = 12  # Binary: 1100
y &= 10  # Binary: 1010, Result: 1000 (8)
print(f"\nBitwise AND: 12 &= 10 = {y}")

# |= (Bitwise OR and assign)
z = 12  # Binary: 1100
z |= 10  # Binary: 1010, Result: 1110 (14)
print(f"Bitwise OR: 12 |= 10 = {z}")

# ^= (Bitwise XOR and assign)
a = 12  # Binary: 1100
a ^= 10  # Binary: 1010, Result: 0110 (6)
print(f"Bitwise XOR: 12 ^= 10 = {a}")

# >>= (Right shift and assign)
b = 10  # Binary: 1010
b >>= 2  # Shift right by 2, Result: 0010 (2)
print(f"Right shift: 10 >>= 2 = {b}")

# <<= (Left shift and assign)
c = 5  # Binary: 0101
c <<= 2  # Shift left by 2, Result: 10100 (20)
print(f"Left shift: 5 <<= 2 = {c}")

# Multiple assignment
p, q, r = 1, 2, 3
print(f"\nMultiple assignment: p={p}, q={q}, r={r}")

# Chained assignment
m = n = o = 100
print(f"Chained assignment: m={m}, n={n}, o={o}")
