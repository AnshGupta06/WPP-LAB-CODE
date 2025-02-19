a = int(input(" Enter The Least Value: "))
b = int(input(" Enter The Max Value: "))
list1 = []
for i in range(a,b+1):

    for j in range (i,b+1):

        list1.append(i ^ j)
print(list1)
print("\n")
print(f"Maximal Value: { max(list1)}")
    