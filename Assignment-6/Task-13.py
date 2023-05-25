# Task-13

def calculator(operator, num_1, num_2):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == '*':
        return num_1 * num_2
    elif operator == '/':
        return num_1 / num_2
    
user_sign = input()
user_num_1 = float(input())
user_num_2 = float(input())

print(calculator(user_sign, user_num_1, user_num_2))