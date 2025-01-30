#QUESTION 1

n = int(input("Enter A Number: "))

global temp 
temp = n

def printsum ( temp , sum = 0) :
    
    remainder = temp%10
    sum = sum + remainder
    temp = temp // 10 

    if temp != 0 :
        printsum(temp , sum)
    elif sum // 10 != 0 :
        temp = sum 
        printsum( temp , sum=0)
    else :
        print(f" Digital Node Of {n} Is { sum } " ) 

#Calling Function
printsum( temp )
