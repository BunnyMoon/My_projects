########################################################################################################################
#Author: Kefa
#Date:04.12
#Task:program which asks the user for the input file’s name;
#reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
#rints a simple histogram in alphabetical order (only non-zero counts should be presented)
#######################################################################################################################

from os import strerror
srcname = input("Open a file:")
#Используем try и except при необходимости написать сообщение об ошибке
try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open the file: ",strerror(e.errno))
    
alpha = 'abcdefghijklmnopqrstuvwxyz' #Добавляем в словарь все буквы английского алфавита
dataDict ={}
for letter in alpha:
    dataDict.update({letter:0})

#Делаем новыое значение, где все буквы будут уже строчными   
data = src.read().strip()
data2 = data.lower()

for ch in data2:
    if ch.isalpha():
        temp = {ch:dataDict[ch]+1}
        dataDict.update(temp)

#Если значение больше 0, то печтаем следующее:
for i in alpha:
    if dataDict[i] > 0:
        print(i,' -> ', dataDict[i])
        
src.close()