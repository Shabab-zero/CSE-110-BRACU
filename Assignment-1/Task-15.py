# Task-15

CGPA = float(input("Enter your CGPA: "))
credits_completed = int(input("Enter number of credits completed: "))

if credits_completed < 30 or CGPA < 3.80:
    print("The student is not eligible for a waiver")
elif CGPA < 3.90:
    print("The student is eligible for a waiver of 25 percent")
elif CGPA < 3.95:
    print("The student is eligible for a waiver of 50 percent")
elif CGPA < 4.00:
    print("The student is eligible for a waiver of 75 percent")
else:
    print("The student is eligible for a waiver of 100 percent")