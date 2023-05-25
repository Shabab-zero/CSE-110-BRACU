# Task-8

input_dictionary_string = input()[1: -1].split(', ')

dictionary = {}
total_value = 0

for items in input_dictionary_string:
        name, value = items.split(':')
        dictionary[name.strip("'")] = int(value)
#       OR:
#       dictionary.update({name.strip("'") : int(value)})
        total_value += int(value)

print('Average is', total_value / len(dictionary))