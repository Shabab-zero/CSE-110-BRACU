# Task-5

def calculate_tax(age, salary, job_designation):
    if age < 18 or job_designation.lower() == 'president' or salary < 10000:
        tax = 0
    elif salary > 10000 and salary < 20000:
        tax = salary * 0.05
    elif salary > 20000:
        tax = salary * 0.1
    return tax

user_age = int(input("Enter your age: "))
user_salary = int(input("Enter your salary: "))
user_job_designation = input("Enter your job designation: ")

print("Your tax:", calculate_tax(user_age, user_salary, user_job_designation))