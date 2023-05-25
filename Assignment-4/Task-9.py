# Task-9

input_string = input("Enter a list: ")
original_list = []
modified_list = []
number = ''

for i in input_string:
    if i == ' ':
        original_list.append(int(number))
        number = ''
    else:
        number += i
original_list.append(int(number))

for i in original_list:
    if i % 2 != 0:
        modified_list.append(i)

print("Original list:", original_list)
print("Modified list:", modified_list)