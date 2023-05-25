# Task-7

def show_palindrome(number):
    palindrome_string = ''
    for i in range(1, number):
        palindrome_string += str(i)
    for i in range(number, 0, -1):
        palindrome_string += str(i)
    return palindrome_string

user_input = int(input())
print(show_palindrome(user_input))