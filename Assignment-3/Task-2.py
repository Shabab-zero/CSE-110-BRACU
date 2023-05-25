# Task-2
input_string = input("Enter a string: ")
input_index = int(input("Enter the index: "))

reversed_string = input_string[input_index: : -1] + input_string[input_index + 1: :]

print("Reversed string:", reversed_string)