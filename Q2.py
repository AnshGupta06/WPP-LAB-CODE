#QUESTION 2 

#IMPORT RANDOM NUMBER
import random
list=[]
count=0

countlist=[]

for i in range (100):
    list.append( random.randint(0,1))

print("List :",list)

for num in list:
    if num == 0 :
        count+=1
    else :
        countlist.append(count)
        count=0
print('\n')
print(countlist )
print('\n')
print('Longest Run of Zeros: \n ')
print(max(countlist))
