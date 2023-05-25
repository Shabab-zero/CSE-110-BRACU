# Task-6

input_number = int(input("Enter a number: "))

sum = 0

for i in range(1, input_number + 1):
    if i % 2 != 0:
        sum += i ** 2
    else:
        sum -= i ** 2

print(sum)