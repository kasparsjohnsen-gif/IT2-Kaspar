import random as r
from YLS_Items import *
from YLS_NPCs import *
gold = 10
day = 0
prestige = 1
persuasion = 1

def main_menu():
    input()


inventory = [

]

def view_inventory(inventory):
    while True:
        for i, Item in enumerate(inventory):
            print(f"{i + 1}: {Item.name}")
        try:
            element_item = int(input("""Which item do you want to inspect
press 0: to close: """))
            if element_item == 0:
                break
            else:
                choosen_item = inventory[element_item - 1]
                item_stats(choosen_item)
        except (ValueError, IndexError):
            print("Invalid item.")

def view_stats():
    while True:
        print(f"""¨¨Stats¨¨
Gold: {gold}
Day: {day}
{"Prestige: " + str(prestige) if prestige > 0 else "\033[A"}
{"Persuasion: " + str(persuasion) if persuasion > 0 else "\033[A"}
""")
        stats_action = input("""Press 1: to view your inventory
Press 0: to exit stats""")
        if stats_action == "1":
            view_inventory(inventory)
        elif stats_action == "0":
            break
        else:
            print("Invalid input")
            True

NPCs = [
    Merchant(), Costumer()
]
def npc_action(npc):
    if type(npc) == Merchant:
        npc.merchant_inventory()
        npc.buy()
        print(1)
    elif type(npc) == Costumer:
        npc.sell()
        print(2)

daytime = True
while daytime == True:
    print(f"""Its Day {day} of owning the shop.
3 people are standing outside the shop""")
    number = 1
    for i in range(2):
        shop_action = input(f"""Press 1: Talk to the {number}. person standing infront of the shop
Press 0: View stats
""")
        if shop_action == "1":
            npc = NPCs[0]
            npc_action(npc)
        elif shop_action == "0":
            view_stats()
        else:
            print("Invalid input")
        number += 1
    daytime = False


print(gold)
print(persuasion)
print(prestige)

