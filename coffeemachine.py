MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def display():
    print(f"water : {resources["water"]}ml")
    print(f"milk : {resources["milk"]}ml")
    print(f"coffee : {resources["coffee"]}g")
    print(f"Money : ${money}")


def insert_coins():
    print("please insert coins : ")
    q = int(input("How many quarters ? "))
    d = int(input("How many dimes ? "))
    n = int(input("How many nickles ? "))
    p = int(input("How many pennies ? "))
    total = (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)
    return total


def check(item):
    one = MENU[item]["ingredients"]["water"] <= resources["water"]
    two = MENU[item]["ingredients"]["coffee"] <= resources["coffee"]
    check1 = one and two
    if item == "espresso":
        return check1
    else:
        check2 = MENU[item]["ingredients"]["milk"] <= resources["milk"]
        return check1 and check2


def consumed(item):
    if item == "espresso":
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]


is_true = True
while is_true:
    choice = input("what would you like to have ? (espresso/latte/cappuccino) : ")
    if choice == "report":
        display()
    elif choice == "off":
        is_true = False
    else:
        paid = insert_coins()
        if check(choice):
            if paid > MENU[choice]["cost"]:
                money += MENU[choice]["cost"]
                change = paid - MENU[choice]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is  your {choice} enjoy!")
                consumed(choice)
            else:
                print("sorry that not enough money.Money refunded.")
        else:
            if MENU[choice]["water"] <= resources["water"]:
                print("there is no enough water.")
            if MENU[choice]["coffee"] <= resources["coffee"]:
                print("there is no enough coffe.")
            if MENU[choice]["milk"] <= resources["milk"]:
                print("there is no enough milk.")
