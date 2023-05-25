# Task-9

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
input_marks = int(input("Enter your marks: "))
higher_exam_marks = {}

for name, marks in exam_marks.items():
    if marks >= input_marks:
        higher_exam_marks.update({name: marks})

print(higher_exam_marks)