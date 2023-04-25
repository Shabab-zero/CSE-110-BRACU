# Task-23(ungraded)

temp_in_F = int(input("Enter the temparature in degrees Fahrenheit: "))

temp_in_C = (temp_in_F - 32) * 0.56

print(temp_in_C, "degrees C")

if temp_in_C < 20:
  print("Winter")

elif temp_in_C <= 25:
  print("Autumn")

elif temp_in_C < 30:
  print("Spring")

else:
  print("Summer")