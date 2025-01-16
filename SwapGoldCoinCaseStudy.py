i = input(" Enter The Number Of Test Cases : ")
i = int(i) 

while i != 0 :

    N,X,S = input(" Enter The Number Of Boxes And Position Of Gold Coin And Number Of Swap Respectively : ").split()
    N = int( N)
    X = int( X)
    S = int ( S)

    # N = int(input(" Enter Number Of Boxes: "))

    # X = int(input(" Enter Position Of Gold Coin: "))

    # S = int(input(" Enter Number Of Swap: "))
    
    i = i-1  

    while  S != 0 :

        a,b = input(" Enter The swap position of box: ").split()
        a= int(a)
        b= int(b)
        if a==X :  X=b
        elif  b==X :  X=a
        S = S - 1      
    print(" Final Positon Of Box: ",X)
    
