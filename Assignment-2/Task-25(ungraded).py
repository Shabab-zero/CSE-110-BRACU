# Task-25(ungraded)

N = int(input("Enter a number: "))
a, b = 0, 1
print(a, b, end = ' ')

while True:
    next_number = a + b
    if next_number > N:
        break
    print(next_number, end = ' ')
    a = b
    b = next_number