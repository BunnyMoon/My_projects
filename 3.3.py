#The bubble sort
#list to sort
list = int(input("How many numbers do you want to add to the list? Enter number: "))
my_list = []

for i in range(list):
    my_list.append(int(input("Enter the number: ")))
print("Your list: ", my_list)   

#increased
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list [i] > my_list [i+1]:
            swapped = True
            my_list [i] , my_list [i+1] = my_list [i+1] , my_list [i]

print("Sort list: ", my_list)

#reverse
r_list  = my_list.copy() 
length = len(r_list) -1

for i in range(length):
    if i < length - i:
        r_list[i], r_list[length - i] = r_list[length - i],r_list[i]
    else:   break    

print("Sort reverse: ", r_list) 

#Standard sort

my_list.sort()
print("Standart sort: ", my_list)


my_list.reverse()
print("Standart reverse: ", my_list)