# n = int(input(" Enter  A Number Of letter: "))
# list=[]
# for i in range (n) :
#     word = input( "Enter A letter: ")
#     list.append(word)   
# i=0
# while i<n :  
#     list[i] = chr( ord(list[i]) - 32 )
#     i=i+2
# print(list)

string_1 = input(" Enter A Word: ")
result =''

for i in range(len(string_1)):
    if i%2 ==0: 
        result+= string_1[i].upper()
    else:
        result+= string_1[i].lower()

print(result) 