# Task-16(ungraded)

a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
user_input = input("Input anything: ")

for list in a_tuple:
    list[-1] = user_input

print(a_tuple)