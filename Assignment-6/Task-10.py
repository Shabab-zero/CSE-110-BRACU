# Task-10

def make_square(number_range):
    dictionary = {}
    for i in range(number_range[0], number_range[1] + 1):
        dictionary.update({i: i ** 2})
    return dictionary

print(make_square((5,9)))