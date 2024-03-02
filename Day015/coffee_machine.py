#it is a coffee machine program
#this prog have some function like report,off(break) also declare quater,nikel,dime,penny

from coffee_list import MENU, resources

QUARTER = 0.25
NICKEL = 0.05
PENNIE = 0.01
DIME = 0.10

def report():
    """this function will print the resources of the coffee machine"""
    print(f"water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {resources["money"]}")

def resource_check(coffee):
    """this function will check the resources of the coffee machine"""
    for item in MENU[coffee]["ingredients"]:
        if resources[item] < MENU[coffee]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def balance_count():
    """this funciton will count the balance after the payment"""
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * QUARTER) + (dimes * DIME) + (nickels * NICKEL) + (pennies * PENNIE)
    return total

def transaction(coffee, total):
    """this function will check the payment and give the coffee also return the change"""
    if total >= MENU[coffee]["cost"]:
        print(f"here is your {coffee} ☕️. Enjoy!")
        resources["money"] += MENU[coffee]["cost"]
        if total >MENU[coffee]["cost"]:
            change = round((total - MENU[coffee]["cost"]),2)
            print(f"here is your change {change}")
        for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return
 
def refil():
    """this function will refil the coffee machine"""
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
    }  
    return resources 

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off":
        print("The coffee machine is off")
        exit()
    elif coffee == "report":
        report()
    elif coffee == "refil":
        resources=refil()
    elif coffee not in MENU:
        print("Invalid input")
    else:
        check = resource_check(coffee)

        if check:
            total = balance_count()
            transaction(coffee, total)