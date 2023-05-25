# Task-19(ungraded)

given_list = [(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]
dictionary = {}

for i, j in given_list:
    if j in dictionary:
        dictionary[j].append((i, j))
    else:
        dictionary.update({j: [(i, j)]})

print(dictionary)