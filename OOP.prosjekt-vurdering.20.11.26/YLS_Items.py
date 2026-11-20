from YLS_Base_stats import *

def prestige_persuasion_check():
    global inventory, prestige, persuasion
    prestige = 0
    persuasion = 0
    prestige_multiplier = 0
    persuasion_multiplier= 0
    for item in inventory:
        prestige += item.prestige
    for item in inventory:
        persuasion += item.persuasion
    for item in inventory:
        if item.abilities == Item.multiplier:
            item.abilities(*item.params)
    prestige *= prestige_multiplier
    persuasion *= persuasion_multiplier

def daily_abilities_check():
    global inventory
    for item in inventory:
        if item.abilities != None:
            if item.abilities != Item.multiplier:
                item.abilities(*item.params)

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
        if self.base_sell_value > 0:
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
Common_Items = [
    # Food
    Item("Half-Eaten Sandwich", "Common", "Food", 5, 3, "Someone took a bite and decided they weren't hungry anymore"),
    Item("Expired Energy Drink", "Common", "Food", 6, 3, "Probably expired three months ago, but it still has some fizz"),
    Item("Instant Noodles", "Common", "Food", 4, 3, "A college student's favourite meal"),
    Item("Slightly Rotten Banana", "Common", "Food", 3, 2, "It's mostly brown, but hey, it's still edible"),

    # Tech
    Item("Old Nokia Phone", "Common", "Tech", 8, 6, "Survived a nuclear apocalypse, but can't run YouTube"),
    Item("Broken Headphones", "Common", "Tech", 5, 3, "Only one side works, but that's better than nothing"),
    Item("USB Stick", "Common", "Tech", 7, 5, "Contains 2GB of questionable files"),
    Item("Wired Mouse", "Common", "Tech", 6, 4, "A perfectly normal computer mouse"),

    # Gear
    Item("Rusty Compass", "Common", "Gear", 7, 5, "Points north... most of the time"),
    Item("Old Backpack", "Common", "Gear", 9, 7, "Smells weird, but has plenty of storage"),
    Item("Wooden Walking Stick", "Common", "Gear", 5, 4, "Perfect for old people and adventurers"),
    Item("Cheap Sunglasses", "Common", "Gear", 6, 4, "Makes you look 10% cooler"),

    # Furniture
    Item("Old Wooden Chair", "Common", "Furniture", 5, 4, "Your mothers Old Wooden Chair"),
    Item("Plastic Garden Chair", "Common", "Furniture", 6, 4, "A classic chair found in every garden"),
    Item("Small Wooden Table", "Common", "Furniture", 9, 7, "Nothing special, but it gets the job done"),
    Item("Old Bookshelf", "Common", "Furniture", 8, 5, "Filled with books nobody has read"),

    # Clothing
    Item("Baseball Cap", "Common", "Clothing", 7, 6, "Just a stylish Baseball Cap", persuasion=1),
    Item("Dirty White T-Shirt", "Common", "Clothing", 5, 3, "Was white once, probably"),
    Item("Old Jeans", "Common", "Clothing", 8, 6, "A little worn out, but still fashionable"),
    Item("Woolly Socks", "Common", "Clothing", 4, 3, "Keeps your feet warm, what more could you ask for?")
]

UnCommon_Items = [

    # Food
    Item("Homemade Apple Pie", "UnCommon", "Food", 14, 11, "Freshly baked by someone's grandmother", persuasion=4),
    Item("Spagetti bolognese", "UnCommon", "Food", 10, 10, "Made by your local chef, tastes wonderfull", persuasion=3, abilities=Item.shrinking_value, params=(1,), abilities_info="Looses 1 gold resell value every day"),

    # Tech
    Item("Mechanical Keyboard", "UnCommon", "Tech", 17, 14, "Sounds like a machine when typing", persuasion=5),
    Item("Vintage Game Console", "UnCommon", "Tech", 16, 13, "An old gaming console that's still in pretty good condition", prestige=8),

    # Gear
    Item("Leather Backpack", "UnCommon", "Gear", 15, 12, "A well-made backpack with plenty of storage", prestige=5),
    Item("Silver Pocket Watch", "UnCommon", "Gear", 18, 15, "An old pocket watch that still works perfectly", prestige=8),

    # Furniture
    Item("Antique Wooden Cabinet", "UnCommon", "Furniture", 16, 13, "An old cabinet in surprisingly good condition", prestige=8),
    Item("Comfortable Recliner", "UnCommon", "Furniture", 14, 11, "A very comfortable chair that practically swallows you"),

    # Clothing
    Item("Designer Hoodie", "UnCommon", "Clothing", 18, 15, "A popular hoodie from a fairly expensive brand", persuasion=8),
    Item("Yamasks Mask", "UnCommon", "Clothing", 10, 8, "Found in a dumpster outside a therapy clinic", prestige=10),
]

Rare_Items = [
    # Food
    Item("Aged Wine Cheese", "Rare", "Food", 25, 21, "Aged for several years and sold at a surprisingly high price", persuasion=12),
    Item("Imported Truffle", "Rare", "Food", 28, 23, "A rare ingredient used by expensive restaurants"),

    # Tech
    Item("Oled Monitor", "Rare", "Tech", 20, 15, "Once you go Oled you can never go back", prestige=25),
    Item("Prototype Smartphone", "Rare", "Tech", 27, 22, "An unreleased phone that somehow ended up on the market", abilities=Item.growing_value, params=(2,), abilities_info="Gain 2 gold resell value every day"),

    # Gear
    Item("Professional Camera", "Rare", "Gear", 25, 21, "A professional camera used by experienced photographers", prestige=15),
    Item("Gold Pocket Watch", "Rare", "Gear", 29, 24, "A beautifully crafted pocket watch made from real gold", prestige=18),

    # Furniture
    Item("Handcrafted Dining Table", "Rare", "Furniture", 28, 23, "A large dining table made from expensive wood", prestige=15),
    Item("Antique Grandfather Clock", "Rare", "Furniture", 30, 25, "An old grandfather clock that still keeps perfect time", abilities=Item.passive_income, params=(2,), abilities_info="Generates 2 gold every day"),

    # Clothing
    Item("Fedora", "Rare", "Clothing", 15, 12, "Worn by a beaver, a cool beaver", persuasion=15),
    Item("Expensive Business Suit", "Rare", "Clothing", 27, 22, "A professionally tailored suit worn by successful businessmen", prestige=15, persuasion=8)
]

Legendary_Items = [
    Item("Stylish Cactus", "Legendary", "Furniture", 33, 27, "The best item in the game. Ofc its a Cactus, what else did you expect?", prestige=50, abilities=Item.multiplier, params=(1.3, "prestige"), abilities_info="Gain 30% more prestige as long as you have this item"),
    Item("Lebrons Basketball", "Legendary", "Gear", 100, 100, "Lebron Lebron Lebroooooonnn Lebron", prestige=20),
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