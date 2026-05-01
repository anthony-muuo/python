MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# check if resources are available
def check_resources(resources, ordered):
    for item in ordered["ingredients"]:
        if resources[item] < ordered["ingredients"][item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True

def check_money(total_amount , cost):
    if total_amount >= cost:
        balance = round(total_amount - cost, 2)
        if balance > 0:
            print(f"Here is ${balance} in change")
            return True
    else:
        print("Sorry that's not enough money. Money refunded!")
        return False

# reduce resources
money= 0
def reduce_resources(resources, ordered, money):
    for item in ordered["ingredients"]:
        resources[item] -= ordered["ingredients"][item]
    money += ordered["cost"]
    return money

# repeadetly...
while True:
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
        continue

    if choice == 'off':
        print("You have successfully stopped the machine")
        break

    if choice not in MENU:
        print("Invalid choice")
        continue

    drink = MENU[choice]

    if check_resources(resources, drink):
        print("Please insert coins:")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        total_amt = round(quarters + dimes + nickels + pennies, 2)

        if check_money(total_amount=total_amt, cost=drink['cost']):
            #update the money by reducing the resources
            money = reduce_resources(resources, drink, money)
            print(f"Here is your {choice} ☕")
