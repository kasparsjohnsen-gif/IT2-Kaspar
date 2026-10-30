import random as r
gold = 10
day = 0

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
    Item("Baseball Cap", "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1)
]
Uncommen_Items = [
    Item("Old Wooden Chair", "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]
Rare_Items = [

]
Legendary_Items = [

]

inventory = [
    Item("Baseball Cap", "Clothing", 3, 2, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]

for element in inventory:
    global prestige
    prestige += Item.prestige

for element in inventory:
    global persuasion
    persuasion += Item.persuasion

def view_inventory(inventory):
    while True:
        for i, Item in enumerate(inventory):
            print(f"{i + 1}: {Item.name}")
        try:
            element_item = int(input("""Which item do you want to inspect
press 0 to close: """))
            if element_item == "0":
                break
            else:
                inspected_item = inventory[element_item - 1]
# "\033[A" printer linjen en oppover
                print(f'''
¨¨{inspected_item.name}¨¨
Itemtype: {inspected_item.catagory}
Worth: {inspected_item.base_sell_value} gold 
{"Prestige: " + str(inspected_item.prestige) if inspected_item.prestige > 0 else "\033[A"}
{"Persuasion: " + str(inspected_item.persuasion) if inspected_item.persuasion > 0 else "\033[A"}
"{inspected_item.info}"
''')
        except (ValueError, IndexError):
            print("Ugyldig item.")
            return None

def choose_from_inventory(inventory):
    for i, Item in enumerate(inventory):
        print(f"{i + 1}: {Item.name}")
    try:
        global sold_item
        sold_item = int(input("Which item do you want to sell?: "))
        return inventory[sold_item - 1]
    except (ValueError, IndexError):
        print("Ugyldig item.")
        return None

class NPC:
    def __init__(self, name, catagory, trait, obsession):
        self.name = name
        self.catagory = catagory
        self.obsession = obsession
        self.trait = trait

    def sell(self):
        print("Hey do you have anything in store for me?")
        choosen_item = choose_from_inventory(inventory)
        print(f"You sold: {choosen_item.name}")
        global gold
        gold += choosen_item.base_sell_value
        del inventory[sold_item - 1]

    def NPC_action(self):
        if self.catagory == "merchant":
            self.sell()
        elif self.catagory == "costumer":
            print()

NPCs = [
    NPC("NPC1", "", "", "")
]

view_inventory(inventory)
NPCs[0].sell()

for item in inventory:
    print(item.name)
print(gold)




""" 
    base_sell_value / sell_action
 """

"""
tall = r.randint(100,200) / 100
"""
