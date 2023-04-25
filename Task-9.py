# Task-9

number = int(input("Enter number of seconds: "))

hours = number // 3600
minutes = (number % 3600) // 60
seconds = (number % 3600) % 60

print("Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)