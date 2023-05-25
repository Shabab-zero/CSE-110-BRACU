# Task-29(ungraded)

m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

devisor = int(input("devisor: "))

product_list = []

for i in range(m, n + 1):
    product = 1
    for j in str(i):
        product = product * int(j)
    product_list.append(product)        

for i in product_list:
    if i % devisor == 0:
        print(i, end = ' ')