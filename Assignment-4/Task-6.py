# Task-6

input_list = input("Enter a list: ")[1: -1].split(', ')
input_list_int = []

for i in input_list:
    input_list_int.append(int(i))

largest_number = input_list_int[0]

for i in range(1, len(input_list_int)):
    if input_list_int[i] > largest_number:
        largest_number = input_list_int[i]
        largest_number_index = i

print("My list:", input_list_int)
print(f"Largest number in the list is {largest_number} which was found at index {largest_number_index}.")