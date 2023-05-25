# Task-18(ungraded)

def divisor_sum(start, end, div1, div2):
    sum_of_devisors = 0

    for i in range(start, end):
        if i % div1 == 0 and i % div2 == 0:
            continue
        elif i % div1 == 0 or i % div2 == 0:
            sum_of_devisors += i

    return sum_of_devisors

starting_value = int(input("Enter starting value: "))
ending_value = int(input("Enter ending value: "))
first_divisor = int(input("Enter first divisor: "))
second_divisor = int(input("Enter second divisor: "))

print(divisor_sum(starting_value, ending_value, first_divisor, second_divisor))