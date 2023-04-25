# Task-14

meters = int(input("Enter distance in meters: "))
seconds = int(input("Enter time in seconds: "))

km = meters / 1000
hours = seconds / 3600

velocity = km / hours

print(velocity,"km/h")

if velocity < 60:
    print("Too slow. Needs more changes.")

elif velocity <= 90:
    print("Velocity is okay. The car is ready!")

else:
    print("Too fast. Only a few changes should suffice.")