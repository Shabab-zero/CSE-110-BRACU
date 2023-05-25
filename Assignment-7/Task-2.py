# Task-2

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

for i in range(len(my_list) - 1):
    min_num = my_list[i]
    min_idx = i
    for j in range(i, len(my_list)):
        if my_list[j] < min_num:
            min_num = my_list[j]
            min_idx = j
    temp = my_list[i]
    my_list[i] = min_num
    my_list[min_idx] = temp

print(my_list)