# Task-9

import math

def area_circumference_generator(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return area, circumference

user_input = float(input("Enter the radius: "))
area, circumference = area_circumference_generator(user_input)

print(area_circumference_generator(user_input))
print(f"Area of the circle is {area} and circumference is {circumference}")