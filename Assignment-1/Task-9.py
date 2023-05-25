# Task-9

number = int(input("Enter time in seconds: "))

hours = number // 3600
minutes = (number % 3600) // 60
seconds = (number % 3600) % 60

#OR:
#hours = (number // 60) // 60
#minutes = (number // 60) % 60
#seconds = number % 60

print(f"Hours: {hours}; Minutes: {minutes}; Seconds: {seconds}")