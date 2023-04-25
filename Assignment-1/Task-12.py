# Task-12

time = int(input("Enter meal time: "))

if time > 23 or time < 0:
    print("Wrong time")

elif time >= 4 and time <= 6:
    print("Breakfast")

elif time == 12 or time == 13:
    print("Lunch")

elif time == 16 or time == 17:
    print("Snacks")

elif time == 19 or time == 20:
    print("Dinner")

else:
    print("Patience is a virtue")