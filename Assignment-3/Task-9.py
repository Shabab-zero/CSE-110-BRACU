# Task-9

input_string = input("Enter a string: ")

for i in range(len(input_string)):
    if input_string[i] == input_string[i - 1]:
        continue
    else:
        print(input_string[i], end = '')