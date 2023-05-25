# Task-4

given_list = input("Enter a list: ")[1: -1:].split(', ')
squired_list = []

for i in given_list:
    squired_list.append(int(i) ** 2)

print(squired_list)