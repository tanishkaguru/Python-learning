print("""🇼​​​​​🇪​​​​​🇱​​​​​🇨​​​​​🇴​​​​​🇲​​​​​🇪​​​​​ 🇹​​​​​🇴​​​​​
╭━━━━┳╮╱╭┳━━━╮╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮╭╮╱╭┳━━━┳╮╱╭┳━━━┳━━━┳╮
┃╭╮╭╮┃┃╱┃┃╭━━╯┃╭━╮┃╭━╮┃╭━━┫╭━━┫╭━━┫╭━━╯┃┃╱┃┃╭━╮┃┃╱┃┃╭━╮┃╭━━┫┃
╰╯┃┃╰┫╰━╯┃╰━━╮┃┃╱╰┫┃╱┃┃╰━━┫╰━━┫╰━━┫╰━━╮┃╰━╯┃┃╱┃┃┃╱┃┃╰━━┫╰━━┫┃
╱╱┃┃╱┃╭━╮┃╭━━╯┃┃╱╭┫┃╱┃┃╭━━┫╭━━┫╭━━┫╭━━╯┃╭━╮┃┃╱┃┃┃╱┃┣━━╮┃╭━━┻╯
╱╱┃┃╱┃┃╱┃┃╰━━╮┃╰━╯┃╰━╯┃┃╱╱┃┃╱╱┃╰━━┫╰━━╮┃┃╱┃┃╰━╯┃╰━╯┃╰━╯┃╰━━┳╮
╱╱╰╯╱╰╯╱╰┻━━━╯╰━━━┻━━━┻╯╱╱╰╯╱╱╰━━━┻━━━╯╰╯╱╰┻━━━┻━━━┻━━━┻━━━┻╯\n""")
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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_res(coffee):
    global resources
    for item in coffee["ingredients"]:
        if resources[item]<coffee["ingredients"][item]:
            print(f"\nSorry there is not enough {item}.\n")
            return False
    return True

def processCoins():
    tot=0.0
    quart=int(input("Enter quarters: "))
    tot+=0.25*quart
    dime=int(input("Enter dimes: "))
    tot+=0.10*dime
    nick=int(input("Enter nickels: "))
    tot+=0.05*nick
    penn=int(input("Enter pennies: "))
    tot+=0.01*penn
    return tot

def deduct_res(coffee):
    global resources
    for item in coffee["ingredients"]:
        resources[item]-=coffee['ingredients'][item]
        

ch=0

while ch==0:
    choice= input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        ch=1
        break
    elif choice=="report":
        print(f"""Water: {resources['water']}
Milk: {resources['milk']}
Coffee: {resources['coffee']}
Money: {profit}
""")
    else:
        coffee=MENU[choice]
        res=check_res(coffee)
        if res is True:
            payment=processCoins()
            if payment<coffee["cost"]:
                print("Sorry, that's not enough money. Refunded!\n")
            else:
                if payment>coffee["cost"]:
                    print(f"\nMoney refunded. ${round(payment-coffee['cost'],2)}")
                profit+=coffee["cost"]
                deduct_res(coffee)
                print(f"\nHere is your {choice}☕!\n")
                
