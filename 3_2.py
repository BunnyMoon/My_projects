#step 1
beatles = []
print("Step 1:", beatles)

#step2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

#step3
for i in range(2):
    if i ==0:
        beatles.append(("Stu_Sutcliffe"))
    else:
        beatles.append("Pete_Best")
print("Step 3:", beatles)

#step4
for i in range(2):
    del beatles[-1]

print("Step 4:", beatles)

#step5
beatles.insert(0, 'Ringo Star')
print("Step 5:", beatles)


#testing list len
print("The Fab", len(beatles))