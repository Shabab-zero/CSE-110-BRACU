# Task-11

input_string = input("Enter a string: ")[1: -1].lower().replace(' ', '')
frequency_dictionary = {}

for character in input_string:
    if character in frequency_dictionary:
        frequency_dictionary[character] += 1
    else:
        frequency_dictionary.update({character: 1})
    
print(frequency_dictionary)