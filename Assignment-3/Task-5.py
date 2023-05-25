# Task-5

input_string = input("Enter a string: ")

for i in range(len(input_string)):
    for j in range(i + 1):
        print(input_string[j], end = '')
    print()