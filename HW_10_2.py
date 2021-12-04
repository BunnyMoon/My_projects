########################################################################################################################
#Author: Kefa
#Date:04.12
#Task: s to make some amendments, which generate the following results:
#• the output histogram will be sorted based on the 
#characters' frequency (the bigger counter should 
#be presented first)
#• the histogram should be sent to a file with the 
#same name as the input one, but with the suffix 
#'.hist' (it should be concatenated to the original 
#name)
#######################################################################################################################

from os import strerror
srcname = input("Open a file: ")
dstname = input("Select a dst file: ")
try:
    src = open(srcname, 'rt')
    dst = open(dstname, 'wt')
except IOError as e:
    print("Cannot open the file: ",strerror(e.errno))
    
alpha = 'abcdefghijklmnopqrstuvwxyz'
dataDict ={}
for letter in alpha:
    dataDict.update({letter:0})
    
data = src.read().strip()
data2 = data.lower()

for ch in data2:
    if ch.isalpha():
        temp = {ch:dataDict[ch]+1}
        dataDict.update(temp)

# 10.2

#Все полученные данные переводим в список и сортируем значения больше 0
valueList = list(dataDict.values())
valueList.sort()
sortedValue = list(filter(lambda x: x > 0, valueList))

#Все отобранные значения передаем в список acendValue и получаем обратную сортировку
acendValue = []
for i in range(0,len(sortedValue)):
    acendValue.append(sortedValue.pop())

for item in acendValue:
    for letter in list(dataDict.keys()):
        if dataDict[letter] == item:
            print(letter, ' -> ', item)
            newData = letter + ' -> ' + str(item) + '\n'
            dst.write(newData)
            del dataDict[letter]
            
src.close()
dst.close()