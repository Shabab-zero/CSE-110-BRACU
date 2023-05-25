# Task-12

def max_twice(list):
    new_list = []
    for i in list:
        if new_list.count(i) < 2:
            new_list.append(i)
    elements_removed = len(list) - len(new_list)
    print("Removed:", elements_removed)
    return new_list

print(max_twice([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))