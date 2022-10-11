from menu_CoffeeMachine_OOP import Menu, MenuItem
from coffee_maker_CoffeeMachine_OOP import CoffeeMaker
from money_machine_CoffeeMachine_OOP import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

play=True
while play:
    order_name = input(f"What would you like? {menu.get_items()}: ").lower()
    if order_name == "off":
        print("Bye!")
        play=False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name=="latte" or order_name=="espresso" or order_name=="cappuccino":
        if coffee_maker.is_resource_sufficient(menu.find_drink(order_name)):
            if money_machine.make_payment(menu.find_drink(order_name).cost):
                coffee_maker.make_coffee(menu.find_drink(order_name))










