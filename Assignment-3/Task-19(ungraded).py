# Task-19(ungraded)

input_string = input('Enter a string: ')

new_string = ''

for i in input_string:
    if i.isalpha():
        if len(new_string) == 0 or last_alpha.islower():
            new_string += i.upper()
            last_alpha = i.upper()
        else:
            new_string += i.lower()
            last_alpha = i.lower()
    else:
        new_string += i

print(new_string)