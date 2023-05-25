# Task-15

def grocery_store(order_items, location = "Dhanmondi"):
    menu_items = {
        'Rice': 105,
        'Potato': 20,
        'Chicken': 250,
        'Beef': 510,
        'Oil': 85
    }
    amount_to_be_paid = 0

    for item in order_items:
        amount_to_be_paid += menu_items[item]

    amount_to_be_paid += 30 if location == "Dhanmondi" else 70

    return amount_to_be_paid

print(grocery_store(["Rice", "Beef", "Rice"]))