# Task-13

input_number = int(input("Enter a number: "))
devisors = 1

for i in range(1, input_number):
    if input_number % i == 0:
        print(i, end = ', ')
        devisors += 1

print(input_number)
print(f"Total {devisors} devisors")