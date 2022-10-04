from menu_coffeemachine import MENU, resources

print(resources)

machine_water = resources['water']
machine_milk = resources['milk']
machine_coffee = resources['coffee']

def doing_coffe():
    global resources
    if machine_water>=resources['water']:
        resources['water']=machine_water-current_drink_water
        resources['coffee']=machine_coffee-current_drink_coffee
        resources['milk'] = machine_milk - current_drink_milk
        return f"Enjoy your {coffee_type}!"
    else:
        return "No watter"



play=True
while play:
    coffee_type = input("What type? espresso/latte/cappuccino: ").lower()
    current_drink_water = MENU[coffee_type]['ingredients']['water']
    current_drink_coffee = MENU[coffee_type]['ingredients']['coffee']
    current_drink_milk = MENU[coffee_type]['ingredients']['milk']
    if resources['water'] <= 0 or resources['coffee'] <= 0 or resources['milk'] <= 0:
        print("OUPS smth wrong")
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        print(doing_coffe())
        print(resources)
    elif coffee_type == "off":
        play=False









