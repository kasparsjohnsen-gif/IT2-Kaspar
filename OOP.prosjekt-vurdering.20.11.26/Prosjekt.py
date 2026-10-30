import random as r
gold = 10



def main_menu():
    input()

""" 
class Item:
    name1: str
    catagory1: str
    base_buy_value1: int
 """


class Item:
    def __init__(self, name, catagory, base_buy_value, base_sell_value, info, prestige=0, charisma=0, abilities=None):
        self.name = name
        self.catagory = catagory
        self.base_buy_value = base_buy_value
        self.base_sell_value = base_sell_value
        self.info = info
        self.prestige = prestige
        self.charisma = charisma
        self.abilities = abilities


# All items
Commen_Items = [
    Item("Baseball Cap", "Clothing", 3, 2, "Just a stylish Baseball Cap", charisma=1)
]
Uncommen_Items = [
    Item("Old Wooden Chair", "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]
Rare_Items = [

]
Legendary_Items = [

]

inventory = [
    Item("Baseball Cap", "Clothing", 3, 2, "Just a stylish Baseball Cap", charisma=1),
    Item("Old Wooden Chair", "Furniture", 3, 2, "Your mothers Old Wooden Chair")
]



def choose_from_inventory(inventory):
    for i, Item in enumerate(inventory):
            print(f"{i + 1}: {Item.name}")
    try:
        global k
        k = int(input("Which item do you want to sell?: "))
        return inventory[k - 1]
    except (ValueError, IndexError):
        print("Ugyldig item.")
        return None




class NPC:
    def __init__(self, name, catagory, trait, obsession):
        self.name = name
        self.catagory = catagory
        self.obsession = obsession
        self.trait = trait

    def sell():
        print("Hey do you have anything in store for me?")
        choosen_item = choose_from_inventory(inventory)
        print(f"You sold: {choosen_item.name}")
        del inventory[k - 1]

    def NPC_action(self):
        if self.catagory == "merchant":
            print()
        elif self.catagory == "costumer":
            print()




for item in inventory:
    print(item.name)





""" 
    base_sell_value / sell_action
 """