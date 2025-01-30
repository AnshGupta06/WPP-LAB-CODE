n = int(input("Enter Number Of Test Cases: "))
list = []
store =[]
count = 0
sum =0

for i in range (0,n):
    number = int(input("Enter Number: "))
    list.append(number)

print(list)

for i in range (0,n):
    temp = list[i]
    count = 0
    while temp!=0 :
        remainder = temp%10
        sum = sum + remainder
        temp = temp // 10 

        if( list[i] % remainder == 0 and remainder != 0 ):
            count = count + 1
    store.append(count)

for i in range (len(store)):
    print(store[i])    
            

    