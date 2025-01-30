#QUESTION 2

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) 
    return fib_sequence

def checkfibonacci (n , ele , j=0):

    for i in range(n):

        temp = []
        temp = fibonacci( ele[i] * 2 )

        count = 0

        for item in temp :

            if item == ele[j] :
                count+=1
                print(" IsFibo")
                break            
    
        j = j +1
        if count == 0 :
            print(" Is Not Fibo ")

# // -1 means last element
# // -2 means last second element
# Generate the first 10 Fibonacci numbers
print(fibonacci(10))

n = int(input("Enter Number Of Test Cases: "))
ele = []
# j=0
for i in range(n):
    ele.append( int(input("Enter The Number: ")))

checkfibonacci ( n , ele )
