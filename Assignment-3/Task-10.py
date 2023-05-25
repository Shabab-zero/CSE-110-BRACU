# Task-10

input_string1, input_string2 = input("Enter a string: ").split(', ')
new_string = ''

if len(input_string1) < len(input_string2):
    for i in range(len(input_string1)):
        new_string += input_string1[i] + input_string2[i]
    new_string += input_string2[len(input_string1): :]
else:
    for i in range(len(input_string2)):
        new_string += input_string1[i] + input_string2[i]
    new_string += input_string1[len(input_string2): :]

print(new_string)