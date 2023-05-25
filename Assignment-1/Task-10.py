# Task-10

hours_worked = int(input("Enter number of hours worked: "))

if hours_worked < 0:
    print("Hour cannot be negative")
elif hours_worked > 168:
    print("Impossible to work more than 168 hours weekly")
elif hours_worked <= 40:
    salary = hours_worked * 200
    print(salary)
else:
    salary = 8000 + (hours_worked - 40) * 300
    print(salary)