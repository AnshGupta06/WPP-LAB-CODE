n = int(input("Enter Number Of Test Cases: "))
list1 = []

for i in range (n) :

    num= int(input("Enter Number Of Cuts: "))

    if num%2 != 0 :
        
        ans = (num + 1)/ 2
        list1.append( ans*(ans-1))
    else :
        ans = num / 2
        list1.append( ans*ans )
        
print( list1 )