# Task-10

input_number = int(input("Enter a number: "))

while True:
    output_number = input_number % 10
    input_number = input_number // 10
    if input_number == 0:
        print(output_number)
        break
    print(output_number, end = ', ')