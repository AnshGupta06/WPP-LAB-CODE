#QUESTION 4

number1,number2 = input(" Enter First And Second Number: ").split()
number1 = int(number1)
number2 = int(number2)

number2 = number1 + number2
number1 = number2 - number1
number2 = number2 - number1

print("After Swap")
print(" First Number: ",number1)
print(" Second Number: ",number2)

