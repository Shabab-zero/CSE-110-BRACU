# Task-19(ungraded)

list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

list_of_unique_elements = []

for i in list_one:
    if i not in list_of_unique_elements:
        list_of_unique_elements.append(i)

for i in list_two:
    if i not in list_of_unique_elements:
        list_of_unique_elements.append(i)

print(list_of_unique_elements)