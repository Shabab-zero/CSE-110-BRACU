# Task-4

def upper_lower(string):
    num_of_uppercase_letters = 0
    num_of_lowercase_letters = 0

    for i in string:
        if i.isupper():
            num_of_uppercase_letters += 1
        elif i.islower():
            num_of_lowercase_letters += 1

    print("No. of Uppercase characters:", num_of_uppercase_letters)
    print("No. of lowercase characters:", num_of_lowercase_letters)

user_input = input()
upper_lower(user_input)