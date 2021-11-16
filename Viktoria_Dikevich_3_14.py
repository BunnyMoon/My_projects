bits = int(input("Enter binary number (ex.0101010111): "), 2)
mask = int('110', 2)

results = bits ^ mask

print(bin(results))