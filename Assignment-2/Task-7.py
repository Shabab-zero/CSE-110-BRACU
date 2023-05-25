# Task-7

print("Enter 10 numbers: ")

total = 0
odd_numbers = 0

for i in range(10):
    number = int(input())
    if number % 2 != 0:
        total += number
        odd_numbers += 1

print(f"The total of the odd numbers is {total} and their average is {total / odd_numbers}")