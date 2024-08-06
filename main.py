from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
obj = CoffeeMaker()
print(obj.report())
menu = Menu()
money = MoneyMachine()
is_true = True
while is_true:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_true = False
    elif choice == "report":
        obj.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if obj.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            obj.make_coffee(drink)
