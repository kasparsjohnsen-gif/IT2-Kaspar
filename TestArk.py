import random as r
while True:
    try: 
        try_amount = int(input(f"""How much do you want to buy it for? (Type 0: to exit)\n"""))
        if try_amount == 0:
            print('"Ahh its ok, I have more things you can look at anyways"')
            break
        elif try_amount < 0:
            print('Invalid Input')
    except (ValueError):
        print("balright")

prestige = 0
persuasion = 0

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
                print("Frutigo aero yams")
                return True
            else:
                return False
        elif choice == "0":
            break
        else:
            print("Invalid input")
            True

""" 
hagling(10, 9, "persuasion")
hagling(10, 11, "prestige")
hagling(10, 5, "persuasion")
hagling(10, 20, "prestige")

y = round((14.52 * (0.64**(((11 + (11 * (prestige / 50))) / 10)*10-10)))*10)
print(y)



prestige = 25
persuasion = 25

hagling(10, 9, "persuasion")
hagling(10, 11, "prestige")
hagling(10, 5, "persuasion")
hagling(10, 20, "prestige")
 """

verdict = hagling(10, 11, "prestige", True)

if verdict == True:
    print("Yippi")