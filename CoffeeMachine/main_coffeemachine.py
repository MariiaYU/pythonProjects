from menu_coffeemachine import MENU, resources
def doing_coffe():
    global resources
    machine_water = resources['water']
    machine_milk = resources['milk']
    machine_coffee = resources['coffee']
    resources['water'] = machine_water-current_drink_water
    resources['coffee'] = machine_coffee-current_drink_coffee
    resources['milk'] = machine_milk - current_drink_milk

    return f"Enjoy your {coffee_type}!"

def user_cash(a,b,c,d):
    user_money=0.25*a + 0.1*b + 0.05*c + 0.01*d
    return user_money

def find_type(type):
    global current_drink_water,current_drink_coffee,current_drink_milk
    current_drink_water = MENU[type]['ingredients']['water']
    current_drink_coffee = MENU[type]['ingredients']['coffee']
    current_drink_milk = MENU[type]['ingredients']['milk']

money_machine = 0
play=True
while play:
    coffee_type = input("What would you like? espresso/latte/cappuccino: ").lower()
    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        find_type(coffee_type)
        if resources['water'] < current_drink_water:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < current_drink_coffee:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < current_drink_milk:
            print("Sorry there is not enough milk.")
        else:
            money_need = MENU[coffee_type]['cost']
            print(f"Please insert coins. Cost of {coffee_type} is {money_need}")
            quarter = int(input("How many quarters($0,25)?: "))
            dime = int(input("How many quarters($0,10)?: "))
            nickle = int(input("How many nickles($0,05)?: "))
            penny = int(input("How many pennies($0,01)?: "))
            user_add=float(user_cash(quarter, dime, nickle, penny))
            if user_add<money_need:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money_machine += float(user_add-money_need)
                print(doing_coffe())
    elif coffee_type == "off":
        play = False
    elif coffee_type == "report":
        print(f"Machine resources: {resources}")
        money_machine = float("{:.2f}".format(money_machine))
        print(f"Money: {money_machine}")












