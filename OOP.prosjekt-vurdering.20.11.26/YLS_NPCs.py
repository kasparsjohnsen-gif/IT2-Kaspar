from pathlib import Path
from YLS_Items import *
import random as r

BASE_DIR = Path(__file__).parent
NAMES_FILE = BASE_DIR / "Names.txt"

def load_names(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

names = load_names(NAMES_FILE)

Obsession = ["Furniture", "Clothing", "Gear", "Food", "Tech"]

def hagling(base_value, try_value, persuasion_or_prestige, obsession_status):
    global persuasion, prestige
    while True:
        if persuasion_or_prestige == "persuasion":
            haggle = round((14.52 * (0.64**((base_value / (try_value + (try_value * (prestige / 50))))*10-10)))*10)
            if obsession_status == True:
                    haggle * 0.8
        elif persuasion_or_prestige == "prestige":
            haggle = round((14.52 * (0.64**((try_value / (base_value + (base_value * (prestige / 50))))*10-10)))*10)
            if obsession_status == True:
                    haggle * 1.3
        if haggle > 100:
            haggle == 100
        print(f"You have a {haggle}% chance of succsesfully hagling npc.name")
        choice = input("""Do you want to proceed with your offer?
Type 1: Yes, Type 0: No
""")
        if choice == "1":
            verdict = r.randint(1,100)
            if haggle >= verdict:
                return True
            else:
                return False
        elif choice == "0":
            break
        else:
            print("Invalid input")
            True


class NPC:
    def __init__(self):
        self.name = r.choice(names)
        self.obsession = r.choice(Obsession)
        self.patience = r.randint(1,4)

class Merchant(NPC):
    def __init__(self):
        super().__init__()
        self.stock = r.randint(2,5)
        self.items_for_sale = self.merchant_inventory()

    def merchant_inventory(self):
        Merchant_inventory = []
        for i in range(self.stock):
            rarity = r.randint(1,20)
            if 10 > rarity >= 1:
                random_index = r.randint(0, len(Commen_Items)-1)
                Merchant_inventory.append(Commen_Items[random_index])
            elif 17 > rarity >= 10:
                random_index = r.randint(0, len(Uncommen_Items)-1)
                Merchant_inventory.append(Uncommen_Items[random_index])
            elif 20 > rarity >= 17:
                random_index = r.randint(0, len(Rare_Items)-1)
                Merchant_inventory.append(Rare_Items[random_index])
            elif rarity == 20:
                random_index = r.randint(0, len(Legendary_Items)-1)
                Merchant_inventory.append(Legendary_Items[random_index])
        return Merchant_inventory  

    def buy(self):
        global inventory, gold
        print(f'"Hi!, my name is {self.name}, and I was wondering if you would be interested in buying anything from me?"')
        left_in_stock = len(self.items_for_sale)
        while left_in_stock > 0:
            for i, Item in enumerate(self.items_for_sale):
                    print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to look at? (type 0 to exit the NPC): """))
                if element_item == 0:
                    print('''"You dont want any more of my items?
I guess ill just have to find someone else to buy them, bye bye!"
*The NPC left*''')
                    break
                else:
                    choosen_item = self.items_for_sale[element_item - 1]
                    if choosen_item.catagory == self.obsession:
                        obsessed = True
                    else:
                        obsessed = False
                    print(f'"Heres my {choosen_item.name}, I can give it to you for {choosen_item.base_buy_value} gold"')
                    item_stats(choosen_item)
                    print(f"You have {gold} gold")
                    while True:
                        try: 
                            try_amount = int(input(f"""How much do you want to buy it for? (Type 0: to exit)\n"""))
                            if try_amount == 0:
                                print('"Ahh its ok, I have more things you can look at anyways"')
                                break
                            elif try_amount < 0:
                                print('Invalid Input')
                            else:
                                haggle = hagling(choosen_item.base_buy_value, try_amount, "persuasion",obsessed)
                                if haggle == True:
                                    inventory.append(choosen_item)
                                    prestige_persuasion_check()
                                    gold -= try_amount
                                    del self.items_for_sale[element_item - 1]
                                    left_in_stock -= 1
                                    print(f'''You bought {choosen_item} for {try_amount} gold
"Much appreciated"''')
                                elif haggle == False:
                                    print(f'''"Are you trying to scam me!?"
"I will now no longer be selling you the {choosen_item}''')
                                    del self.items_for_sale[element_item - 1]
                                    left_in_stock -= 1
                        except (ValueError):
                            print("Invalid Input.")
                        break
            except (ValueError, IndexError):
                print("Invalid item.")
        print(f'''"Ill be going now Bye"
{self.name} left''')


class Costumer(NPC):
    def __init__(self):
        super().__init__()
        self.spending_limit = r.randint(2,4)
        self.patience = r.randint(2,4)
        

    def sell(self):
        global inventory, gold
        print(f'"Hey!, my name is {self.name}, and I was wondering if you have anything in store for me?"')
        while self.patience > 0:
            for i, Item in enumerate(inventory):
                print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to sell?: """))
                if element_item == 0:
                    print('''"You dont have anything!?
well i guess ill just get going then
Bye"''')
                    break
                else:
                    choosen_item = inventory[element_item - 1]
                    if choosen_item.catagory == self.obsession:
                        obsessed = True
                    else:
                        obsessed = False
                    while True:
                            try: 
                                try_amount = int(input(f"""How much do you want to sell {choosen_item} for? (Type 0: to exit)\n"""))
                                if try_amount == 0:
                                    print('"Ahh its ok, I have more things you can look at anyways"')
                                    break
                                elif try_amount < 0:
                                    print('Invalid Input')
                                else:
                                    haggle = hagling(choosen_item.base_sell_value, try_amount, "prestige", obsessed)
                                    if haggle == True:
                                        gold += try_amount
                                        del inventory[element_item - 1]
                                        prestige_persuasion_check()
                                        print(f"You sold {choosen_item.name} for {try_amount} and now have {gold} gold")
                                        self.spending_limit -= 1
                                        break
                                    elif haggle == False:
                                        print("You are scaming me arent you!?")
                                        self.patience -= 1
                                        break    
                            except (ValueError):
                                print("Invalid Input.")
            except (ValueError, IndexError):
                print("Invalid item.")
        print(f'''"Ill be going now Bye"
{self.name} left''')

class Businessman(NPC):
    def __init__(self):
        super().__init__()
        self.deal = 1

