# Task-10

input_list = input("Enter a list: ").split(', ')
input_list_int = []
modified_list = []

for i in input_list:
    input_list_int.append(int(i))

for i in input_list_int:
    if i not in modified_list:
        modified_list.append(i)

print("Input list:", input_list_int)
print("Modified list:", modified_list)