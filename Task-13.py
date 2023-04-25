# Task-13

marks = int(input("Enter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid")

elif marks >= 90:
    print("A")

elif marks >= 80:
    print("B")

elif marks >= 70:
    print("C")

elif marks >= 60:
    print("D")

elif marks >= 50:
    print("E")

else:
    print("F")