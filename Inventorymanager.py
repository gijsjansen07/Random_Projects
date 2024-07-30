'''Een inventory met items. Je kunt items toe voegen, veranderen en verwisselen en als je een nummer in typed krijgen'''


inventory = {1:"empty",2:"empty",3:"empty",4:"empty",5:"empty", 6:"empty",7:"empty",8:"empty",9:"empty",10:"empty"}
print (inventory)


def werkelijke_positie(string):
    while True:
            inputpos = input(string)
            try:
                inputpos = int(inputpos)
                if inputpos < 1 or inputpos> 10:
                    print("type een getal tussen de 1 - 10. ")
                else:
                    break; 
            except ValueError:
                print("type een getal tussen de 1 - 10. ")
    return inputpos

def Items_Toevoegen(items, posities):
    for n in range(len(items)):
        inventory[posities[n]] = items[n]
    return inventory

def posities_vragen_voor_toevoegen():
    posities = []
    
    for n in items:
        posities.append(werkelijke_positie(f'Positie van {n} '))

    return posities

def New_Items_bepalen(type):
    
    for n in range(type):

        var = input("Item ")
        if var == "|":
            break; 
        else:
            items.append(var)
    return items 
    
def Wissel_Items_bepalen():
    wissel_items = []
    for n in range(2):
        
        wissel_items.append(werkelijke_positie(f'Item positie {n + 1} die je wilt switchen '))
    return wissel_items

    
def Items_wisselen(wissel_items):
    temp_item = inventory[wissel_items[0]]
    inventory[wissel_items[0]] = inventory[wissel_items[1]]
    inventory[wissel_items[1]] = temp_item
    return inventory
    
while True:
    ipt = input("command ")
    if ipt == "Vtoevoegen":
        items = []
        print(Items_Toevoegen(New_Items_bepalen(10),posities_vragen_voor_toevoegen()))
    elif ipt == "1toevoegen":
        items = []
        print(Items_Toevoegen(New_Items_bepalen(1), posities_vragen_voor_toevoegen()))
    elif ipt == "wisselen":
        print(Items_wisselen(Wissel_Items_bepalen()))
    elif ipt == "help":
        Helpdict ={"Vtoevoegen": "10 nieuwe items toevoegen",
               "1toevoegen": "1 nieuw item toevoegen",
               "wisselen": "2 items van positie wisselen"}
        for key in Helpdict:
            print(f'{key} : {Helpdict[key]}')
        
    elif ipt == "|":
        break; 