# QUESTION 1c
list =[]
copy=[]

print(" Integers From 0 To 49: ")
a=2

for i in range (97,123) :
    j=1
    while j<a :
        letter = chr(i)
        list.append(letter)
        j=j+1
    a=a+1


print(list)
