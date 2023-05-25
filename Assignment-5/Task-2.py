# Task-2

input_tuple = input()[1: -1].split(', ')
new_tuple = []

for i in input_tuple:
    new_tuple.append(int(i))

print(tuple(new_tuple[2: -2]))