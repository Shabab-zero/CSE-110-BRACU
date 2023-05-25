# Task-8

def show_palindrome(number):
    palindrome_string = ''
    for i in range(1, number):
        palindrome_string += str(i)
    for i in range(number, 0, -1):
        palindrome_string += str(i)
    return palindrome_string

def show_palindromic_triangle(number):
    for i in range(1, number + 1):
        for j in range(number - i):
            print(' ', end = ' ')
        for m in show_palindrome(i):
            print(m, end = ' ')
        print()

user_input = int(input())
show_palindromic_triangle(user_input)