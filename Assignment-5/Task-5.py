# Task-5

given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
input_number = int(input("Enter a number: "))
instances_of_input_number = 0

for i in given_tuple:
    if i == input_number:
        instances_of_input_number += 1

print(f"{input_number} appears {instances_of_input_number} times in the tuple")

#OR:
#print(input_number, 'appears', given_tuple.count(input_number), 'times in the tuple')