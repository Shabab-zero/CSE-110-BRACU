# Task-17(ungraded)

def remove_odd(number_list):
    list_of_even_numbers = []
    for i in number_list:
        if i % 2 == 0:
            list_of_even_numbers.append(i)

    return list_of_even_numbers

print(remove_odd ([11,2,3,4,5,2,0,5,3]))