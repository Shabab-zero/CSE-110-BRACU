# Task-16

quantity_of_numbers = int(input("Enter quantity of numbers: "))

minimum = maximum = int(input())
sum = minimum

for i in range(quantity_of_numbers - 1):
    number = int(input())
    sum += number
    if number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Avarage is:", sum / quantity_of_numbers)