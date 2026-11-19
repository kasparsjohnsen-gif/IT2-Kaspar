
def prestige_persuasion_check():
    global inventory, prestige, persuasion
    prestige = 0
    persuasion = 0
    for item in inventory:
        prestige += item.prestige
    for item in inventory:
        persuasion += item.persuasion
    prestige * prestige_multiplier
    persuasion * persuasion_multiplier


class Item:
    def __init__(self, name, rarity, catagory, base_buy_value, base_sell_value, info, prestige=0, persuasion=0, abilities=None, params=None, abilities_info=""):
        self.name = name
        self.rarity = rarity
        self.catagory = catagory
        self.base_buy_value = base_buy_value
        self.base_sell_value = base_sell_value
        self.info = info
        self.prestige = prestige
        self.persuasion = persuasion
        self.abilities = abilities
        self.params = params
        self.abilities_info = abilities_info

    # Abilities
    # Activates every Day
    def growing_value(self, value):
        self.base_sell_value += value

    def shrinking_value(self, value):
        self.base_sell_value -= value

    def passive_income(self, value):
        global gold
        gold += value

    # Activates once
    def multiplier(self, value, persusaion_or_prestige):
        global persuasion_multiplier, prestige_multiplier
        if persusaion_or_prestige == "persuasion":
            persuasion_multiplier += value
        elif persusaion_or_prestige == "prestige":
            prestige_multiplier += value


# All items
Commen_Items = [
    Item("Baseball Cap", "Commen", "Clothing", 7, 6, "Just a stylish Baseball Cap", persuasion=1),
    Item("Old Wooden Chair", "Commen", "Furniture", 5, 4, "Your mothers Old Wooden Chair")
]
Uncommen_Items = [
    Item("Yamasks Mask", "Uncommen", "Clothing", 10, 7, "Found in a dumpster outside a therapy clinic", prestige=10)
]
Rare_Items = [
    Item("Fedora", "Rare", "Clothing", 15, 12, "Worn by a beaver, a cool beaver", persuasion=15)
]
Legendary_Items = [
    Item("Stylish Cactus", "Legendary", "Furniture", 33, 27, "The best item in the game. Ofc its a Cactus, what else did you expect?", prestige=50, abillities=Item.multiplier, params=(1.3, "prestige"), ),
    Item("Lebrons Basketball", "Legendary", "Gear", 100, 90, "Lebron Lebron Lebroooooonnn Lebron", prestige=20),
    Item("Golden Crown", "Legendary", "Clothing", 30, 25, "Only worn by Kings, and you I guess...", prestige=5, persuasion=15),
    Item("RTX 6090 ti", "Legendary", "Tech", 60, 30, "The best card of the unreleased new generation, dont ask me how I got it!", abilities=Item.growing_value, params=(10,), abilities_info="Gain 10 gold every day from crypto mining"),
    Item("Enchanted Golden Apple", "Legendary", "Food", 32, 26, "The highest grade apple you can find. One bite from this thing and your tongue becomes golden", persuasion=30)
]


# * betyr at den unpacker
#func((2, 3)) liste med begge to,  func(2, 3) begge som parameters
"""
Inventory[3].abilities(*Inventory.params)
"""

"""
for item in Inventory:
    if item.abilites != None:
        if item.abilities != Item.multiplier:
"""

def item_stats(choosen_item):
# "\033[A" printer linjen en oppover
    print(f'''
¨¨{choosen_item.name}¨¨
Rarity: {choosen_item.rarity}
Itemtype: {choosen_item.catagory}
Resell value: {choosen_item.base_sell_value} gold 
{"Prestige: " + str(choosen_item.prestige) if choosen_item.prestige > 0 else "\033[A"}
{"Persuasion: " + str(choosen_item.persuasion) if choosen_item.persuasion > 0 else "\033[A"}
{"Ability: " + str(choosen_item.abilities_info) if choosen_item.abilities_info != "" else "\033[A"}
"{choosen_item.info}"
''')