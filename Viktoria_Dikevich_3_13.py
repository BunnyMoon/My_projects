bits = int('0101010101', 2)
mask = int('10', 2)

results = bits | mask

print(bin(results), type(bin))