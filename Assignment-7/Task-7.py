# Task-7

list_one = input()[1: -1].split(', ')
list_two = input()[1: -1].split(', ')
merged_list = []

for i in list_one:
    merged_list.append(int(i))
for i in list_two:
    merged_list.append(int(i))

for i in range(1, len(merged_list)):
    for j in range(len(merged_list) - i):
        if merged_list[j + 1] < merged_list[j]:
            temp = merged_list[j]
            merged_list[j] = merged_list[j + 1]
            merged_list[j + 1] = temp

if len(merged_list) % 2 == 0:
    median = (merged_list[len(merged_list) // 2] + merged_list[len(merged_list) // 2 - 1]) / 2
else:
    median = merged_list[len(merged_list) // 2]

print('Sorted list =', merged_list)
print('Median =', median)