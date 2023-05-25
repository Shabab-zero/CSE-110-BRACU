# Task-17(ungraded)

my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
modified_dictionary = {}

for key, value in my_dictionary.items():
    if value != None:
        modified_dictionary[key] = value

print(modified_dictionary)