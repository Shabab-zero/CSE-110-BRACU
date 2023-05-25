# Task-16(ungraded)

def splitting_money(amount):
    money_split = ''
    notes = [500, 100, 50, 20, 10, 5, 2, 1]

    for note in notes:
        quatity = amount // note
        if quatity != 0:
            money_split += f"{note} Taka: {quatity} note(s)\n"
        amount = amount % note

    return money_split

user_input = int(input("Enter money amount: "))
print(splitting_money(user_input))