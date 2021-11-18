# The inner life of lists
list_1 = [1]
list_2 = list_1
print(list_1, list_2)

list_1[0] = 2
print(list_1, list_2)