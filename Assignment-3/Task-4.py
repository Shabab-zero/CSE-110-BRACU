# Task-4

input_string = input("Enter a string: ")

if input_string.endswith('er'):
    print(input_string[: -2: ] + 'est')
elif len(input_string) < 4 or input_string.endswith('est'):
    print(input_string)
else:
    print(input_string + 'er')