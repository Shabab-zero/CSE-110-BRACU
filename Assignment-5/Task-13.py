# Task-13

a_list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

dictionary = {}

for tuple in a_list:
    if tuple[0] in dictionary:
        dictionary[tuple[0]].append(tuple[1])
    else:
        dictionary.update({tuple[0]: [tuple[1]]})

print(dictionary)