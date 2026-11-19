import random as r
from YLS_Items import *
from YLS_NPCs import *
gold = 10
day = 0
prestige = 1
persuasion = 1
inventory = []

def main_menu():
    input()

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

NPCs = [
    Merchant(), Costumer(), Merchant()
]
def npc_action(npc):
    if type(npc) == Merchant:
        npc.merchant_inventory()
        npc.buy()
        print(1)
    elif type(npc) == Costumer:
        npc.sell()
        print(2)

rent_paid = True
while rent_paid == True:
    print(f"""Its Day {day} of owning the shop.
3 people are standing outside the shop""")
    while True:
        _person = ["first", "second", "third"]
        index = 0
        shop_action = input(f"""Press 1: Talk to the {_person[0 + index]}. person standing infront of the shop
Press 0: View stats\n""")
        index += 1
        index1 = 0
        if shop_action == "1":
            npc = NPCs[0 + index1]
            npc_action(npc)
            if index1 < 2:
                index1 += 1
            else:
                print("Theres no more costumers")
                break
        elif shop_action == "0":
            view_stats()
        else:
            print("Invalid input")


print(gold)
print(persuasion)
print(prestige)

