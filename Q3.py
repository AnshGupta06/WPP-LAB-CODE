#QUESTION 3

number = input(" Enter A Number: ")
number = int(number)
multiply = 1

while number!=0 :
    print(number,end='*' if number>1 else '\n')
    multiply = number * multiply 
    number-=1

print(" Factorial of Number: ",multiply)