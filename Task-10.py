# Task-10

hours = int(input("Hours worked: "))

if hours < 0:
    print("Hours can't be negative")

elif hours > 168:
    print("Impossible to work more than 168 hours weekly")

elif hours <= 40:
    salary = hours * 200
    print(salary)

else:
    salary = 8000 + (hours - 40) * 300
    print(salary)