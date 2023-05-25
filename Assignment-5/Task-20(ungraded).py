# Task-20(ungraded)

given_string = input()[1: -1].replace('.', '').split(' ')
special_characters = input()[1: -1].replace("'", '').split(', ')
dictionary = {}

for i in given_string:
    ascii_sum = 0
    for j in i:
        ascii_sum += ord(j)
    index_value = ascii_sum % len(special_characters)
    if special_characters[index_value] not in dictionary.keys():
        dictionary.update({special_characters[index_value]: [i]})
    else:
        if i in dictionary[special_characters[index_value]]:
            continue
        else:
            dictionary[special_characters[index_value]].append(i)

print("Words in the given String:", given_string)
print('Answer:', dictionary)