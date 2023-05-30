#!/usr/bin/python3
import sys
import math

# Functiom to check if a number is prim
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Read the input file
filename = sys.argv[1]
with open(filename, 'r') as file:
    number = int(file.read())

# Find the prime factors
factors = []
for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0 and is_prime(i):
        factors.append((i, number // i))
# Print the factorization
for factor in factors:
    print(f"{number}={factor[0]}*{factor[1]}")
