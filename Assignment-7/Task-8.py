# Task-8

list_one = input()[1: -1].split(', ')
input_list = []
for i in list_one:
    input_list.append(int(i))

closest_to_zero = input_list[0] + input_list[1]

for i in range(len(input_list) - 1):
    if abs(input_list[i] + input_list[i + 1]) < abs(closest_to_zero):
        closest_to_zero = input_list[i] + input_list[i + 1]
        closest_values = [input_list[i], input_list[i + 1]]

print(f"Two pairs which have the smallest sum = {closest_values[0]} and {closest_values[1]}")