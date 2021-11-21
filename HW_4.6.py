#############################################
# Author: Kefa
# Date: 21.11
# Task: write a pair of functions converting
# liters/100km into miles/gallons, and vice versa
#############################################

lit_per_g = 3.785411784
kil_per_m = 1.609344

def convert_mileage(miles_per_gallon):
    '''Преобразовываем мили на галлон в литры на 100 километров "'''
    return (100 * lit_per_g) / (kil_per_m * miles_per_gallon)

def liters_needed(distance_km, miles_per_gallon):
    """Определим кол-во литров, необходимых для расстояния с заданными милями на галлон"""
    lit_per_100km = convert_mileage(miles_per_gallon)
    return lit_per_100km * distance_km / 100

 # Выводим результат
print("Liters needed for 200km with 15mpg:", liters_needed(200, 15))