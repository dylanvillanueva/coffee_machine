MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def enough_resources(drink):
    for ingredient in drink["ingredients"]:
        if resources[ingredient] > drink["ingredients"][ingredient]:
            return True
        else:
            return False


def pay_for_drink(drink):
    drink_cost = drink["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount_deposited = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if amount_deposited > drink_cost:
        change = round(amount_deposited - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]


def report():
    water = f"{resources['water']}ml"
    milk = f"{resources['milk']}ml"
    coffee = f"{resources['coffee']}g"
    message = f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}"
    print(message)


coffee_machine_on = True

while coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        report()
    elif choice == "off":
        coffee_machine_on = False
    else:
        drink = MENU[choice]

        if enough_resources(drink):
            payment_processed = pay_for_drink(drink)
            if payment_processed:
                money += drink["cost"]
                make_coffee(drink)
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry, there is not enough coffee.")