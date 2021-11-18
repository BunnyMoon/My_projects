my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in my_list:
    if i not in new_list: 
        new_list.append(i) # Only ubique numbers will be added
my_list = new_list # To update the original list.

print("Unique elements only:", my_list)
