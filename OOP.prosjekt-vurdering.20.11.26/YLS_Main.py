import random as r
from YLS_Base_stats import *
from YLS_Items import *
from YLS_NPCs import *

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
Rent: {rent}
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
    Merchant(), Customer(), Businessman()
]
# r.choice([Businessman(),Merchant(), Customer()]

def npc_action(npc):
    if type(npc) == Merchant:
        npc.merchant_inventory()
        npc.buy()
    elif type(npc) == Customer:
        npc.sell()
    elif type(npc) == Businessman:
        npc.deal()

print(r"""
__  __                       
\ \/ /___  __  _______       
 \  / __ \/ / / / ___/       
 / / /_/ / /_/ / /           
/_/\____/\__,_/_/          __
   / /   ____  _________ _/ /
  / /   / __ \/ ___/ __ `/ / 
 / /___/ /_/ / /__/ /_/ / /  
/_____/\____/\___/\__,_/_/   
  / ___// /_  ____  ____     
  \__ \/ __ \/ __ \/ __ \    
 ___/ / / / / /_/ / /_/ /    
/____/_/ /_/\____/ .___/     
                /_/
""")

rent = 2
rent_paid = True
try:
    while rent_paid == True:
        print(f"""Its day {day} of owning the shop and the rent is now {rent} gold.
    there is 3 new people standing outside the shop""")
        while True:
            person = ["first", "second", "third"]
            if person_index < 3:
                shop_action = input(f"""Press 1: Talk to the {person[0 + person_index]} person standing infront of the shop
    Press 0: View stats\n""")
                if shop_action == "1":
                    npc = NPCs[0 + npc_index]
                    npc_action(npc)
                elif shop_action == "0":
                    view_stats()
                else:
                    print("Invalid input")   
                person_index += 1 
            else:
                print("Theres no more Customers")
                break

        print("Night has come")
        if rent <= gold:
            gold -= rent
            print(f"You paid rent for {rent} gold ")
        else:
            print()
            rent_paid = False
        rent = round(rent*1.5)
        day += 1
        person_index = 0
        npc_index = 0
        daily_abilities_check()
    print("You lose")
except KeyboardInterrupt:
    print("Exiting the Game")