# Task-11

input_number = int(input("Enter a number: "))

digits = 0

while True:
    input_number = input_number // 10
    digits += 1
    if input_number == 0:
        break

print(digits, 'digits')