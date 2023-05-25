# Task-4

sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]

for i in range(len(sitting_list)):
    for two_k in range(0, len(sitting_list) - 2, 2):
        if sitting_list[two_k] > sitting_list[two_k + 2]:
            temp = sitting_list[two_k]
            sitting_list[two_k] = sitting_list[two_k + 2]
            sitting_list[two_k + 2] = temp
    for two_k_plus_one in range(1, len(sitting_list) - 2, 2):
        if sitting_list[two_k_plus_one] < sitting_list[two_k_plus_one + 2]:
            temp = sitting_list[two_k_plus_one]
            sitting_list[two_k_plus_one] = sitting_list[two_k_plus_one + 2]
            sitting_list[two_k_plus_one + 2] = temp

print(sitting_list)