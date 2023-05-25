# Task-14

def string_div_modify(sentence, position):
    modified_string = sentence[0]

    for i in range(1, len(sentence)):
        if i % position != 0:
            modified_string += sentence[i]
    for i in range(1, len(sentence)):
        if i % position == 0:
            modified_string += sentence[i]

    return modified_string

user_sentence = input()[1: -1]
user_position = int(input())

print(string_div_modify(user_sentence, user_position))