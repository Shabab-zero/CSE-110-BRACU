# Task-1

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

for i in range(1, len(my_list)):
    for j in range(len(my_list) - i):
        if my_list[j + 1] < my_list[j]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp


print(my_list)