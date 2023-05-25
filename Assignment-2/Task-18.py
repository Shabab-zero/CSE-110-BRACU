# Task-18

M = int(input("Enter height/line numbers: "))
N = int(input("Enter length/column numbers: "))

for i in range(M):
    for j in range(1, N + 1):
        print(j, end = '')
    print()