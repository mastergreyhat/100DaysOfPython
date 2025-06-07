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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coins():
    """Returns the total of coins inserted"""
    print("Please insert coins.")
    try:
        total = int(input("How many quarters?: "))*0.25
        total += int(input("How many dimes?: "))*0.1
        total += int(input("How many nickles?: "))*0.05
        total += int(input("How many pennies? "))*0.01
    except ValueError:
        print("Unable to process coins. Please Try again.")
        process_coins()
    return total

def transaction_status(payment, drink_cost):
    global profit
    if payment == drink_cost:
        profit += drink_cost
        return True
    elif payment > drink_cost:
        profit += drink_cost
        balance = round(payment - drink_cost, 2)
        print(f"Here is ${balance} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Updates the report with remaining ingredients"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# refill funcion (not requirement of the course)
def refill(to_refill, quantity):
    global resources
    resources[to_refill] += quantity


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")

# Adding code to refill items (not requirement of the course)
    elif choice == "refill":
        to_refill = input("What do you want to refill? (Water/Milk/Coffee): ").lower()
        quantity = int(input("How much ml/g to refill?: "))
        refill(to_refill, quantity)
    else:
        try:
            drink = MENU[choice]
        except KeyError:
            print("Please Enter a valid item.")
            continue
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_status(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# Basic Error handling is implemented (Further error handling on possible failure blocks should be implemented - not requirement of course)

# In real life scenario, we will be only able to choose from 3 options in the coffee machine, so some of the error handling currently implemented in code might not be required. 