# Task-26(ungraded)

N = int(input("Enter number in dec: "))

binary_number = 0
counter = 0

while N != 0:
    number = (N % 2) * 10 ** counter
    binary_number += number
    counter += 1
    N = N // 2

print("Binary:", binary_number)