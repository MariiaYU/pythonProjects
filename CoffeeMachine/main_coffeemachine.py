from menu_coffeemachine import MENU, resources

print(resources)

def doing_coffe():
    global resources
    machine_water = resources['water']
    machine_milk = resources['milk']
    machine_coffee = resources['coffee']
    resources['water'] = machine_water-current_drink_water
    resources['coffee'] = machine_coffee-current_drink_coffee
    resources['milk'] = machine_milk - current_drink_milk
    return f"Enjoy your {coffee_type}!"



play=True
while play:
    coffee_type = input("What type? espresso/latte/cappuccino: ").lower()
    current_drink_water = MENU[coffee_type]['ingredients']['water']
    current_drink_coffee = MENU[coffee_type]['ingredients']['coffee']
    current_drink_milk = MENU[coffee_type]['ingredients']['milk']
    if resources['water'] < current_drink_water or resources['coffee'] < current_drink_coffee or resources['milk'] <= current_drink_milk:
        print("OUPS smth wrong")
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        print(doing_coffe())
        print(resources)
    elif coffee_type == "off":
        play=False









