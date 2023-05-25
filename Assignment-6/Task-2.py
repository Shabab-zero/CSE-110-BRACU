# Task-2

def fibonacci(limit):
    a, b = 0, 1
    print(a, b, end = ' ')

    while True:
        next_number = a + b
        if next_number > limit:
            break
        print(next_number, end = ' ')
        a = b
        b = next_number

user_input = int(input())
fibonacci(user_input)