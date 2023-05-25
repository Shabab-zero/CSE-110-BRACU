# Task-3

input_number = input("Enter a number: ")
isBinary = True

for i in input_number:
    if i != '0' and i != '1':
        isBinary = False
        print("Not a Binary Number")
        break

if isBinary:
    print("Binary Number")