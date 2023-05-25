# Task-17(ungraded)

input_string = input('Enter a string: ')
input_character = input('Enter a character: ')

initial_index = 0

for i in range(len(input_string)):
    if input_string[i] == input_character:
        print(input_string[initial_index: i:])
        initial_index = i + 1
print(input_string[initial_index: :])