#QUESTION 2

number = input(" Enter A Number: ")
number = int(number)

while number!=0 :
    print(number,end='*' if number>1 else '\n')
    number-=1
