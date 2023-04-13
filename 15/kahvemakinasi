MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def yeterlimi(orderreq):
    for item in resources:
        if MENU[orderreq]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True #ilk return sonrasına bakılmıyor

def parasayar():
    inserted_total = float(input("how many quarters?: ")) * 0.25 + float(input("how many dimes?: ")) * 0.10 + float(input("how many nickles?: ")) * 0.05 + float(input("how many pennies?: ")) * 0.01
    return inserted_total

def report():
    for resource in resources:        
        print(f"{resource}: {resources[resource]}ml")
    print(f"${money}")

def siviyutucu():
    print("Please add resources")
    for resource in resources:
        resources[resource] += float(input(f"how much {resource} to add? "))
        
def kahveyapici(kabzimal):
  if kabzimal == "espresso" or "latte" or "cappuccino":
    for item in resources:        
        resources[item] -= MENU[kabzimal]["ingredients"][item]

        
calismayadevammi = True

while calismayadevammi == True:
    
    cevap = input("Hoşgeldin Adem Günesen, ne istersin? (espresso/latte/cappuccino): ")
    if cevap == "report":
        report()
    elif cevap == "off":
        calismayadevammi = False
    elif cevap == "add":
        print("Please insert bozuk para.")
        money = money =+ parasayar()
        siviyutucu()
    elif cevap == "espresso" or "latte" or "cappuccino":  
        if yeterlimi(cevap):
            print("Please bozuk para.")
            inserted_total = parasayar()
            if inserted_total < MENU[cevap]["cost"]:
                print("Sorry that's not enough bozuk para. Bozuk paralar iade edildi.")
            else:   
                paraustu = inserted_total - MENU[cevap]["cost"]
                print(f"Here is ${paraustu:.2f} in change.")
                print(f"Here is your {cevap} ☕️. Enjoy!")
                money += MENU[cevap]["cost"]
                kahveyapici(cevap)
    else:
       print("Please enter valid input") #burayı çalıştıramadım
