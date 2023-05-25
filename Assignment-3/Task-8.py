# Task-8

input_string = input("Enter a string: ")

for i in range(len(input_string)):
    if i % 2 != 0:
        if ord(input_string[i]) >= 97 and ord(input_string[i]) <= 122:
            print(chr(ord(input_string[i]) - 32), end = '')
        else:
            print(input_string[i], end = '')