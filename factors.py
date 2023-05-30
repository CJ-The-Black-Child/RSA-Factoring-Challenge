import sys

# REad the input file
filename = sys.argv[1]
with open(filename, 'r') as file:
    numbers = file.read().splitlines()

# Factorize the numbers
for number in numbers:
    number = int(number)
    factors = []
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    # print the Factorization
    for factor in factors:
        print(f"{number}={factor[0]}*{factor[1]}")
