# Task-5

input_list = input("Enter a list: ")[2: -2:].split('\", \"')
modified_list = []

for i in input_list:
    if i != '':
        modified_list.append(i)

print("Original list:", input_list)
print("Modified list:", modified_list)