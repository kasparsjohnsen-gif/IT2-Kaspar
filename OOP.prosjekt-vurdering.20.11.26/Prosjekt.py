import random as r
gold = 10
day = 0
prestige = 0
persuasion = 0

def main_menu():
    input()

""" 
class Item:
    name1: str
    catagory1: str
    base_buy_value1: int
 """

class Item:
    def __init__(self, name, rarity, catagory, base_buy_value, base_sell_value, info, prestige=0, persuasion=0, abilities=None):
        self.name = name
        self.name = rarity
        self.catagory = catagory
        self.base_buy_value = base_buy_value
        self.base_sell_value = base_sell_value
        self.info = info
        self.prestige = prestige
        self.persuasion = persuasion
        self.abilities = abilities


# All items
Commen_Items = [
    Item("Baseball Cap", "Commen" "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Commen" "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]
Uncommen_Items = [
    
]
Rare_Items = [
    Item("Fedora", "Rare", "Clothing", 10,6, "Worn by a beaver", persuasion=25)
]
Legendary_Items = [
    Item("Stylish Cactus", "Legendary","Furniture", 20, 14, "The stylishest Cactus you'll ever see", prestige=50)
]

inventory = [
    Item("Baseball Cap", "Commen", "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Commen", "Furniture", 3, 2, "Your mothers Old Wooden Chair"),
    Item("Stylish Cactus", "Legendary", "Furniture", 12, 8, "The stylishest Cactus you'll ever see", prestige=50),
    Item("Fedora", "Rare", "Clothing", 10,6, "Worn by a beaver", persuasion=25)
]

for item in inventory:
    prestige += item.prestige

for item in inventory:
    persuasion += item.persuasion

def item_stats(choosen_item):
# "\033[A" printer linjen en oppover
    print(f'''
¨¨{choosen_item.name}¨¨
Rarity: {choosen_item.rarity}
Itemtype: {choosen_item.catagory}
Worth: {choosen_item.base_sell_value} gold 
{"Prestige: " + str(choosen_item.prestige) if choosen_item.prestige > 0 else "\033[A"}
{"Persuasion: " + str(choosen_item.persuasion) if choosen_item.persuasion > 0 else "\033[A"}
"{choosen_item.info}"
''')

def view_inventory(inventory):
    while True:
        for i, Item in enumerate(inventory):
            print(f"{i + 1}: {Item.name}")
        try:
            element_item = int(input("""Which item do you want to inspect
press 0 to close: """))
            if element_item == 0:
                break
            else:
                choosen_item = inventory[element_item - 1]
                item_stats(choosen_item)
        except (ValueError, IndexError):
            print("Invalid item.")
            return None

class NPC:
    def __init__(self, name, obsession, patience):
        self.name = name
        self.obsession = obsession
        self.patience = patience

class Merchent(NPC):
    def __init__(self, name, obsession, patience, stock):
        super().__init__(name, obsession, patience)
        self.stock = stock

    def merchant_inventory(self):
        Merchant_inventory = []
        for i in range(self.stock):
            rarity = r.randint(1,20)
            if 10 > rarity >= 1:
                random_index = r.randint(0, len(Commen_Items))
                Merchant_inventory.append(Commen_Items[random_index])
            elif 17 > rarity >= 10:
                random_index = r.randint(0, len(Commen_Items))
                Merchant_inventory.append(Uncommen_Items[random_index])
            elif 20 > rarity >= 17:
                random_index = r.randint(0, len(Commen_Items))
                Merchant_inventory.append(Rare_Items[random_index])
            elif rarity == 20:
                random_index = r.randint(0, len(Commen_Items))
                Merchant_inventory.append(Legendary_Items[random_index])
        return Merchant_inventory  

    def buy(self):
        print(f'"Hi!, my name is {self.name}, and I was wondering if you would be interested in buying anything form me?"')
        while True:
            self.merchant_inventory
            for i, Item in enumerate(self.merchant_inventory):
                    print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to look at? (type 0 to exit the NPC): """))
                if element_item == 0:
                    print('''"You dont want any more of my items?
I guess ill just have to find someone else to buy them, bye bye!"
*The NPC left*''')
                    break
                else:
                    choosen_item = self.merchant_inventory[element_item - 1]
                    print(f'"Heres my {choosen_item.name}, I can give it to you for {choosen_item.base_buy_value} gold"')
                    item_stats(choosen_item)
                    choice = input(f"""Buy it for {choosen_item.base_buy_value} gold?
type: 1 for yes or 0 for no""")
                    if choice == "1":
                        global inventory
                        inventory.append(choosen_item)
                        gold -= choosen_item.base_buy_value
                        del self.merchant_inventory[element_item - 1]
                        print(f"You bought {choosen_item} for {choosen_item.base_buy_value} gold")
                    elif choice == "0":
                        print('"Ahh its ok, I have more things you can look at anyways"')
                        True
            except (ValueError, IndexError):
                print("Invalid item.")
                return None


class Costumer(NPC):
    def __init__(self, name, obsession, patience, spending_limit):
        super().__init__(name, obsession, patience)
        self.spending_limit = spending_limit
        

    def sell(self):
        print(f'"Hey!, my name is {self.name}, and Im interested if you have anything in store for me?"')
        while True:
            global inventory
            for i, Item in enumerate(inventory):
                print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to sell?: """))
                if element_item == 0:
                    print('''"You dont have anything Balright, well i guess ill get going then"''')
                    break
                else:
                    global gold
                    sold_item = inventory[element_item - 1]
                    gold_gained = sold_item.base_sell_value
                    gold += gold_gained
                    del inventory[element_item - 1]
                    print(f"You sold {sold_item.name} for {gold_gained} and now have {gold} gold")
            except (ValueError, IndexError):
                print("Invalid item.")
                return None

class Businessman(NPC):
    def __init__(self, name, obsession, patience, deal):
        super().__init__(name, obsession, patience)
        self.deal = deal


NPCs = [
    NPC("NPC1", "", "", "")
]
""" 
def NPC_action(i):
    if NPC[i] == Merchant(NPC):
        .sell()
    elif self.catagory == "costumer":
        self.buy() """

view_inventory(inventory)
NPCs[0].sell()

for item in inventory:
    print(item.name)
print(gold)

print(persuasion)
print(prestige)

""" 
    base_sell_value / sell_action
 """

"""
tall = r.randint(100,200) / 100
"""
