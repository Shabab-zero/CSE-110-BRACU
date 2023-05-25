# Task-7

list_1 = input("Enter a list: ")[1: -1].split(', ')
list_2 = input("Enter another list: ")[1: -1].split(', ')

list_1.pop()
list_1.extend(list_2)
combined_list = []

for i in list_1:
    combined_list.append(int(i))

print(combined_list)