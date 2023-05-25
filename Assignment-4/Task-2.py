# Task-2

input_list = input("Enter a list: ")[1: -1:].split(', ')
input_list_int = []

for i in input_list:
    input_list_int.append(int(i))

if len(input_list_int) >= 4:
    print(input_list_int[2: -2:])
else:
    print("Not possible.")