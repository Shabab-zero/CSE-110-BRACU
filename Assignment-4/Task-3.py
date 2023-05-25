# Task-3
input_list = []

for i in range(5):
    input_list.append(int(input("Enter a number: ")))

print("Input data:", input_list)
print("Printing values from the list in reverse order:")

for i in range(len(input_list) - 1, -1, -1):
    print(input_list[i])