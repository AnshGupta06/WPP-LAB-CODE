#QUESTION 5

number = input(" Enter A Number: ")
number = int(number) 

print("Table Of :",number)

addition=number

while addition <= number*10 :
    print(addition,end=',' if number<number*10 else '\n')
    addition = addition + number 
