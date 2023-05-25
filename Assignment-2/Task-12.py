# Task-12

input_number = int(input("Enter a number: "))
temp = input_number
digits = 0

while True:
    temp = temp // 10
    digits += 1
    if temp == 0:
        break
    
while True:
    output_number = input_number // (10 ** (digits - 1))
    input_number = input_number % (10 ** (digits - 1))
    digits -= 1
    if input_number == 0:
        print(output_number)
        break
    print(output_number, end = ', ')