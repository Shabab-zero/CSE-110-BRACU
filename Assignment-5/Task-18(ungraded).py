# Task-18(ungraded)

a_dict = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}
user_input = input().split(', ')
new_dictionary = {}

for key, Value in a_dict.items():
    if Value >= int(user_input[0]) and Value < int(user_input[1]):
        new_dictionary.update({key: Value})

print(new_dictionary)