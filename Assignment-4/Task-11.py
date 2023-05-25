# Task-11

list_1 = input("Enter a list: ")[1: -1].split(', ')
list_2 = input("Enter another list: ")[1: -1].split(', ')
common_members = False

for i in list_1:
    if i in list_2:
        common_members = True
        break

print(common_members)