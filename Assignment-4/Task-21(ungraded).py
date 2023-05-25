# Task-21

input_list = input("Enter a list: ").split(',')
input_list_int = []
list_of_unique_elements = []

for i in input_list:
    input_list_int.append(int(i))

for i in input_list_int:
    if i not in list_of_unique_elements:
        list_of_unique_elements.append(i)

print("Given numbers in list:", input_list_int)
print("List without any dupliacte values:", list_of_unique_elements)