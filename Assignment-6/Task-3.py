# Task-3

def foo_moo(number):
    if number % 2 == 0 and number % 3 == 0:
        return 'FooMoo'
    elif number % 2 == 0:
        return 'Foo'
    elif number % 3 == 0:
        return 'Moo'
    else:
        return 'Boo'
    
user_input = int(input())
print(foo_moo(user_input))