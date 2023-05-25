# Task-16(ungraded)

input_list = input("Enter a list: ").split(', ')
input_list_int = []

for i in input_list:
    input_list_int.append(int(i))

largest_number = float('-inf')
second_largest_number = float('-inf')

for i in input_list_int:
    if i > largest_number:
        largest_number = i

for i in input_list_int:
    if i != largest_number and i > second_largest_number:
        second_largest_number = i

print("My list", input_list_int)
print(f"Second largest number in the list is {second_largest_number} which was found at index {input_list_int.index(second_largest_number)}.")