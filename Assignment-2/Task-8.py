# Task-8

N = int(input("Enter a number: "))

sum = 0

for i in range(N + 1):
    if i % 7 == 0:
        sum += i

print(sum)