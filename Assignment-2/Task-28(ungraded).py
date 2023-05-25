# Task-28(ungraded)

m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

prime_list = []
perfect_list = []

for i in range(m, n + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(i)

for i in range(m, n + 1):
    sum_of_devisors = 0
    for j in range(1, i):
        if i % j == 0:
            sum_of_devisors += j
    if sum_of_devisors == i:
        perfect_list.append(i)

print(f"Between {m} and {n},")
print(f"Found {len(prime_list)} prime numbers")
print(f"Found {len(perfect_list)} perfect number")
print("Prime numbers:", prime_list)
print("Perfect number:", perfect_list)