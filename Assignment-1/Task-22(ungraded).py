# Task-22(ungraded)

canvases_ordered = int(input("Enter number of canvases ordered: "))
paintTubes_ordered = int(input("Enter number of paint tubes ordered: "))

total_amount = canvases_ordered * 120 + paintTubes_ordered * 75

print("Previous total:", total_amount)

if total_amount >= 1000:
    discount_amount = 150
elif total_amount >= 750:
    discount_amount = 50
elif total_amount >= 500:
    discount_amount = 20
elif total_amount >= 300:
    discount_amount = 10
else:
    discount_amount = 0

print("New total after discount:", total_amount - discount_amount)