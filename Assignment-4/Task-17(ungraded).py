# Task-17(ungraded)

input_list = input("Enter a list: ").split(', ')
input_list_int = []

for i in input_list:
    input_list_int.append(int(i))

largest_value = smallest_value = input_list_int[0]

for i in input_list_int:
    if i > largest_value:
        largest_value = i

for i in input_list_int:
    if i < smallest_value:
        smallest_value = i 

print("My list:", input_list_int)
print(f"Smallest number in the list is {smallest_value} which was found at index {input_list_int.index(smallest_value)}.")
print(f"Largest number in the list is {largest_value} which was found at index {input_list_int.index(largest_value)}.")