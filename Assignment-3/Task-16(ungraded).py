# Task-16(ungraded)

input_string = input('Enter a string: ')
input_character = input('Enter a character: ')

if input_character in input_string:
    for i in input_string:
        if i != input_character:
            print(i, end = '')
elif len(input_string) <= 3:
    print(input_string)
else:
    print(input_string[1: -1: ])