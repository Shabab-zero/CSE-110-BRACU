# Task-5

lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
course_code = input('Course code: ')

marks_info = {}
for item in lst:
    marks_info.update({item[0]: 
                       {'CSE110': item[1], 
                        'PHY111': item[2],
                        'MAT110': item[3]}})

course_info = []

for name, marks in marks_info.items():
    course_info.append((name, marks[course_code]))

for i in range(1, len(course_info)):
    for j in range(len(course_info) - i):
        if course_info[j + 1][1] > course_info[j][1]:
            temp = course_info[j]
            course_info[j] = course_info[j + 1]
            course_info[j + 1] = temp

for name, marks in course_info:
    print(name)