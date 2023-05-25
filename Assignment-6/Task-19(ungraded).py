# Task-19(ungraded)

def char_checker(string):
    test_string = 'abcdefghij'
    for i in test_string:
        if i not in string:
            return 6
    return 5    
    
user_input = input()[1: -1].lower()

for i in range(char_checker(user_input)):
    print("PSG will win the Champions League this season")