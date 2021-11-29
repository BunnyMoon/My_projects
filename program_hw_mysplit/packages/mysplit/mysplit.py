def mysplit(strng):
    A = ""
    B = []
    for i in strng:
        if i != " ":
            A += i
        else:
            if A: # Проверка строки А
                B.append(A)
                A = ""

    # Если А содержит допустимую строку, то добавляем:
    if A:
        B.append(A)
    return(B)

    # Проверка:

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))