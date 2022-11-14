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
profit = 0


# Check resources function
def check_resources():
    """function cross-check the resources of the drink with the resources available."""
    for ingredient in MENU[drink_request]["ingredients"]:
        try:
            if MENU[drink_request]["ingredients"][ingredient] >= resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        except KeyError:
            print("There is no milk in this drink.")
    return True


# Process coins.
def process_coins():
    """function which allows the process of coins and returns total"""
    print("Insert coins: ")
    quarter = int(input("How many quarters: "))
    dime = int(input("How many dimes: "))
    nickel = int(input("How many nickels: "))
    penny = int(input("How many pennies: "))
    total = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickel) + (0.01 * penny)
    return total


def make_drink():
    for i in resources:
        resources[i] = resources[i] - MENU[drink_request]["ingredients"][i]
    print("Here is your latte. Enjoy!")


machine_on = True

while machine_on:
    # TODO 01: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    drink_request = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 02: Turn off the Coffee Machine by entering “off” to the prompt.
    if drink_request == "off":
        machine_on = False

    # TODO 03: Print report.
    elif drink_request == "report":
        message = f"""
        Report on Machine's Resources:
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: ${profit:.2f}
        """
        print(message)

    # TODO 04: Check resources sufficient?
    elif drink_request == "espresso" or drink_request == "latte" or drink_request == "cappuccino":
        if check_resources():
            # TODO 05: Process coins.
            coins_inserted = process_coins()

            # TODO 06: Check transaction successful?
            if coins_inserted < MENU[drink_request]["cost"]:
                print(coins_inserted)
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit = float(profit) + MENU[drink_request]["cost"]
                customer_change = coins_inserted - MENU[drink_request]["cost"]
                print(f"${coins_inserted:.2f}")
                print(f"Here is ${customer_change:.2f} dollars in change.")

                # TODO 07: Make Coffee.
                make_drink()
    else:
        print("Try again, wrong input")
