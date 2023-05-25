# Task-6

my_list = [4, 2, 3, 1, 6, 5]
unsorted_list = my_list.copy()

for i in range(1, len(my_list)):
    for j in range(len(my_list) - i):
        if my_list[j + 1] < my_list[j]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

changed_position = 0

for i in range(len(my_list)):
    if my_list[i] != unsorted_list[i]:
        changed_position += 1

print(changed_position)