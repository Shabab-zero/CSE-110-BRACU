# Task-15

input_number = int(input("Enter a number: "))
isPrime = True

for i in range(2, input_number):
    if input_number % i == 0:
        isPrime = False
        print(input_number, "is not a prime number")
        break

if isPrime == True:
    print(input_number, "is a prime number")