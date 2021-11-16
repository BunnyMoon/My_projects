
def collatz(c0):

    count = 0
    while c0 != 1:
        count += 1
        if c0 % 2 == 0:
            c0 = c0 // 2
        elif c0 % 2 == 1:
            c0 = c0*3 + 1
        print(c0)
    else:
        print("steps = ", count)