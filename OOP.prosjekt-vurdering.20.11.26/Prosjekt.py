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
    def __init__(self, name, catagory, base_buy_value, base_sell_value, info, prestige=0, persuasion=0, abilities=None):
        self.name = name
        self.catagory = catagory
        self.base_buy_value = base_buy_value
        self.base_sell_value = base_sell_value
        self.info = info
        self.prestige = prestige
        self.persuasion = persuasion
        self.abilities = abilities


# All items
Commen_Items = [
    Item("Baseball Cap", "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]
Uncommen_Items = [
    
]
Rare_Items = [
    Item("Fedora", "Clothing", 10,6, "Worn by a beaver", persuasion=25)
]
Legendary_Items = [
    Item("Stylish Cactus","Furniture", 20, 14, "The stylishest Cactus you'll ever see", prestige=50)
]

inventory = [
    Item("Baseball Cap", "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Furniture", 3, 2, "Your mothers Old Wooden Chair"),
    Item("Stylish Cactus","Furniture", 12, 8, "The stylishest Cactus you'll ever see", prestige=50),
    Item("Fedora", "Clothing", 10,6, "Worn by a beaver", persuasion=25)
]

for item in inventory:
    prestige += item.prestige

for item in inventory:
    persuasion += item.persuasion

def item_stats(choosen_item):
# "\033[A" printer linjen en oppover
    print(f'''
¨¨{choosen_item.name}¨¨
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

def choose_from_inventory(inventory):
    while True:
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

class NPC:
    def __init__(self, name, catagory, trait, obsession):
        self.name = name
        self.catagory = catagory
        self.obsession = obsession
        self.trait = trait

    def sell(self):
        print('"Hey do you have anything in store for me?"')
        choose_from_inventory(inventory)
        

    def NPC_inventory(self):
        NPC_inventory = []
        for i in range(r.randint(2,4)):
            x = r.randint(1,20)
            if 10 > x >= 1:
                random_index = r.randint(0, len(Commen_Items))
                NPC_inventory.append(Commen_Items[random_index])
            elif 17 > x >= 10:
                random_index = r.randint(0, len(Commen_Items))
                NPC_inventory.append(Uncommen_Items[random_index])
            elif 20 > x >= 17:
                random_index = r.randint(0, len(Commen_Items))
                NPC_inventory.append(Rare_Items[random_index])
            elif x == 20:
                random_index = r.randint(0, len(Commen_Items))
                NPC_inventory.append(Legendary_Items[random_index])    

    def buy(self):
        while True:
            self.NPC_inventory
            for i, Item in enumerate(self.NPC_inventory):
                    print(f"{i + 1}: {Item.name}")
            try:
                element_item = int(input("""Which item do you want to look at? (type 0 to exit the NPC): """))
                if element_item == 0:
                    print('''"You dont want any more of my items?
I guess ill just have to find someone else to buy them, bye bye!"
*The NPC left*''')
                    break
                else:
                    choosen_item = inventory[element_item - 1]
                    print(f'"Heres my {choosen_item}, I can give it to you for {choosen_item.base_buy_value} gold"')
                    item_stats(choosen_item)
                    choice = input(f"""Buy it for {choosen_item.base_buy_value} gold?
type: 1 for yes or 0 for no""")
                    if choice == "1":
                        inventory.append(choosen_item)
                        gold -= choosen_item.base_buy_value
                        print(f"You bought {choosen_item} for {choosen_item.base_buy_value} gold")
                    elif choice == "0":
                        True
            except (ValueError, IndexError):
                print("Invalid item.")
                return None
        
        

    
    def NPC_action(self):
        if self.catagory == "merchant":
            self.sell()
        elif self.catagory == "costumer":
            self.buy()

NPCs = [
    NPC("NPC1", "", "", "")
]

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
