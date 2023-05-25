# Task-18(ungraded)

list_1 = input("Enter a list: ").split(', ')
list_2 = input("Enter another list: ").split(', ')

list_of_common_elements = []

for i in list_1:
    if i in list_2:
        list_of_common_elements.append(i)

print(list_of_common_elements)