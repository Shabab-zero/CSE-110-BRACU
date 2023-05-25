# Task-7

number = int(input("Enter a number: "))

if number % 2 == 0 and number % 5 == 0:
    print("Multiple of 2 and 5 both")
elif number % 2 == 0 or number % 5 == 0:
    print(number)
else:
    print("Not a multiple we want")