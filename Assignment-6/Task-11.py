# Task-11

def rem_duplicate(a_tuple):
    a_list = []
    for i in a_tuple:
        if i not in a_list:
            a_list.append(i)

    return tuple(a_list)

print(rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2])))