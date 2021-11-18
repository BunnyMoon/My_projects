s = input("Enter your numbers: ")
print("Your input:", s)

lis = s.split() # Split
print("Your input after split:", lis)

numbers = []
for num in lis:
    numbers.append(int(num))
print("After append in list:", numbers)

print("Sum(list):", sum(numbers))