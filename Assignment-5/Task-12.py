# Task-12

given_dictionary = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
number_of_items = 0

for key in given_dictionary:
    for items in given_dictionary[key]:
        number_of_items += 1

print("Number of items:", number_of_items)