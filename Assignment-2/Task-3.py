# Task-3

sum = 0

#OR:
#i = 0
#while True:
#    if i == 600:
#        break
#    i = i + 1
#    if i % 7 == 0 and i % 9 == 0:
#        sum = sum + i

for i in range(601):
    if i % 7 == 0 and i % 9 == 0:
        sum = sum + i

print(sum)