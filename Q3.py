#QUESTION 3 

def UtopianTree( n , growth = 1 ):

    if n==0 : 
        print(1)

    while n > 0 :

        growth = growth * 2
        n = n-1

        if n  > 0 :
            growth = growth + 1
            n = n - 1
            if n > 0 :
                UtopianTree( n , growth )
                n = 0 #very important ,,, that why numbers are not repeting
            else :
                print( growth )
                break
        else :
            print( growth )
            break

t = int( input("Enter The Number OF Test Cases: "))
list = []

for i in range (t):

    list.append( int(input("Enter Number Of Growth Cycles: ")) )

for i in range (t):

    UtopianTree(  list[i] )

