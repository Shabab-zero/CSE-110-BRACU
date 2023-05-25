# Task-27(ungraded)

N = int(input("Enter number in bin: "))

decimal_number = 0
counter = 0

while N != 0:
    number = (N % 10) * 2 ** counter
    counter += 1
    N = N // 10
    decimal_number += number

print("Decimal:", decimal_number)