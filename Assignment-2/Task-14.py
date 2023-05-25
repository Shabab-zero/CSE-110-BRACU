# Task-14

input_number = int(input("Enter a number: "))
sum_of_devisors = 0

for i in range(1, input_number):
    if input_number % i == 0:
        sum_of_devisors += i

if sum_of_devisors == input_number:
    print(input_number, "is a perfect number")
else:
    print(input_number, "is not a perfect number")