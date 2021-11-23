#Some simple functions: evaluating the BMI
def bmi(weight, height):
    if weight or height <= 0:
        return None
    
    return weight / height ** 2


print(bmi(0, 0))
print(bmi(4, 4))
print(bmi(-99, 1.65))
print(bmi(0, -10))
print(bmi(52.5, 1.65))
