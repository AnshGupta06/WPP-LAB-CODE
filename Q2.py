dict = {}

n = int(input("Enter The Number Of Product: "))

for i in range(0,n):
    name = input("Enter Product Name: ")
    price = input("Enter Product Price: ")

    dict.update( { name : price } )

print(dict)


ask = input("Product Name: ")
print(dict[ask])
