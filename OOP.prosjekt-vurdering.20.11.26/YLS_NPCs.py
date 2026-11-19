from pathlib import Path
from YLS_Items import *
from YLS_Base_stats import *
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
I guess ill just have to find someone else to buy them!"''')
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
                            elif try_amount > choosen_item.base_buy_value:
                                print("Are you stupid?")
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
        deals = [self.deal_1, self.deal_2, self.deal_3]
        self.deal = r.choice(deals)

    def deal_1(self):
        global gold
        print(f'''"Hello my name is {self.name}, I have a Deal for you"
    "if you can lend me 10 gold Ill go and invest it right now"
    "and defenetly not gamble it *wink* *wink* and then you can get half of the profits"
    "Is that a deal?"''')
        print(f"You have {gold}")
        if gold < 10:
            print('"You dont have enough money sadly"')
        else:
            choice = input("Type 1: Yes, Type 0: No")
            if choice == "1":
                gold -= 10
                print('You lose 10 gold\n"Nice your not gonna be disappointed"')
                outcome = r.randint(1,50)
                if 1 <= outcome < 11:
                    print('''"Yoo, Im back"\n"So bad news I kinda lost it all"\n"My Bad"''')
                elif 11 <= outcome < 21:
                    print('"Yoo, Im back"\n"So good news I didnt lose everything"\n"Bad news I only have half of what you gave me back"\n"so here"\n*He gives you back 5 gold*')
                    gold += 5
                elif 21 <= outcome < 26:
                    print('"Yoo, Im back"\n"Bro I managed to dobbel the money soo i guess you can have the money back "\n*He gives you back 10 gold*')
                    gold += 10                
                elif 26 <= outcome < 31:
                    print('"Yoo, Im back"\n"Bro I managed to win"\n"you can get back your money plus an extra 5 gold"\n*He gives you back 15 gold*')
                    gold += 15
                elif 31 <= outcome < 41:
                    print('"Yoo, Im back"\n"Bro I managed to win quite a bit"\n"you can get back your money plus an extra 10 gold"\n*He gives you back 20 gold*')
                    gold += 20
                elif 41 <= outcome < 46:
                    print('"Yoo, Im back"\n"Bro I managed to win big"\n"you can get back your money plus an extra 15 gold"\n*He gives you back 25 gold*')
                    gold += 25
                elif 46 <= outcome < 49:
                    print('"Yoo, Im back"\n"Bro I managed to win big"\n"you can get back your money plus an extra 20 gold"\n*He gives you back 30 gold*')
                    gold += 30
                elif outcome == 49:
                    print('"Yoo, Im back"\n"Bro You dont know how locked in I was back there!"\n"I won 200 gold!!"\n"heres your share of 100 gold"\n*He gives you back 100 gold*')
                    gold += 100
                elif outcome == 50:
                    print('"Yoo, Im back"\n"Bro I won everything im loaded!!!"\n"I won 500 gold!!!!"\n"heres your share of 250 gold"\n*He gives you back 250 gold*')
                    gold += 250
                print(f"You now have {gold} gold")
            elif choice == "0":
                print('"You dont want to take the deal?"\n"your loss I guess"\n"Bye!"')
            else:
                print("Invalid Input")
        print(f'''"Ill be going now Bye"
{self.name} left''')

    def deal_2(self):
        global inventory, gold
        print(f'''"Whats up my name is {self.name}, and I have a Deal for you"
    "If you can sell me all your items Ill pay you 1.5 times their worth"''')
        choice = input("Sell all your items\nType 1: Yes, Type 0")
        if choice == "1":
            print('"Great hand me over your Items"')
            total_gold = 0
            for item in inventory:
                total_gold += round(item.base_sell_value * 1.5)
            inventory.clear()
            gold += total_gold
            print(f'"Thank you for the Deal heres {total_gold} gold for all your items\nYou gained {total_gold} and now have {gold} gold"')
        elif choice == "0":
            print('"You dont want to take the deal?"\n"your loss I guess"\n"Bye!"')
        else:
            print("Invalid Input")
        print(f'''"Ill be going now Bye"
{self.name} left''')


    def deal_3(self):
        global inventory, gold
        print(f'''"Hi my name is {self.name}, and I have a Deal for you"
    if you pay me 75 gold Ill give you a random Legendary Item"''') 
        choice = input('"So what do you say, will you take the deal?"\nType 1: Yes, Type 0: No')
        if choice == "1":
            if gold < 75:
                print("You dont have enough money sadly")
            else:
                gold -= 75
                random_index = r.randint(0, len(Legendary_Items)-1)
                inventory.append(Legendary_Items[random_index])
                print(f'"Great, heres your Legendary item: {Legendary_Items[random_index].name}"')
        elif choice == "0":
            print('"You dont want to take the deal?"\n"your loss I guess"\n"Bye!"')
        else:
            print("Invalid Input")
        print(f'''"Ill be going now Bye"
{self.name} left''')

    
