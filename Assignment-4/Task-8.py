# Task-8

list_1 = input("Enter a list: ")[1: -1].split(', ')
list_2 = input("Enter another list: ")[1: -1].split(', ')

combined_list = list_1 + list_2
list_of_even_elements = []

for i in combined_list:
    if int(i) % 2 == 0:
        list_of_even_elements.append(int(i))

print(list_of_even_elements)