#QUESTION 5

list=[]
reverse=[]

n = int(input(" Enter The Number Of Students: \n"))

for i in range (n) :

    ele= input()
    ele = ele[: 15]
    list.append(ele)

# list = list[::-1]
# print("The names of the students are: \n",list)

# Another Method
for i in list:
    reverse.append(i[::-1])

print("The names of the students are: \n ",reverse)