# Task-22(ungraded)

canvases = int(input("Enter the number of canvases: "))
paint_tubes = int (input("Enter the number of paint tubes: "))

total = canvases * 120 + paint_tubes * 75

print("Previous total:", total)

if total < 300:
  print("New total after discount:", total)

elif total < 500:
  print("New total after discount:", total - 10)

elif total < 750:
  print("New total after discount:", total - 20)

elif total < 1000:
  print("New total after discount:", total - 50)

else:
  print("New total after discount: ", total - 150)