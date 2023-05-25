# Task-6

def years_months_days(number_of_days):
    years = number_of_days // 365
    months = (number_of_days % 365) // 30
    days = (number_of_days % 365) % 30

    print(f"{years} years, {months} months and {days} days")

user_input = int(input("Enter number of days: "))
years_months_days(user_input)