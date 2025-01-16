#QUESTION 6

number = input(" Enter A Number: ")
number = int(number)

sum = 0
rem = 1

while number > 0 :
    rem= number%10
    sum = sum*10 + rem 
    number = number // 10

print(" REVERSE OF NUMBER: ",sum)