import random as r
import time as t

#Dictianary
values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}

shoe = []

for key in values.keys():
    for k in range(0, 16):
        shoe.append(key)

r.shuffle(shoe)

print(shoe)
# Player's and Dealer's card in str
pcard1 = shoe.pop(0)
dcard1 = shoe.pop(0)
pcard2 = shoe.pop(0)
dcard2 = shoe.pop(0)
pecard = shoe.pop(0)
decard = shoe.pop(0)

# Player's and Dealer's card in int
intpcard1 = int(values[pcard1])
intdcard1 = int(values[dcard1])
intpcard2 = int(values[pcard2])
intdcard2 = int(values[dcard2])
intpecard = int(values[pecard])
intdecard = int(values[decard])

paces = 0
daces = 0
phand = intpcard1 + intpcard2
dhand = intdcard1 + intdcard2
pbust = False
dbust = False
end = False

# If you spawn with 2 aces
if phand > 21:
    phand -= 10
    paces += 1
if dhand > 21:
    dhand -= 10
    daces += 1

# Counts aces in your hand
if pcard1 == "A":
    paces += 1
if pcard2 == "A":
    paces += 1
if dcard1 == "A":
    daces += 1
if dcard2 == "A":
    daces += 1
if pecard == "A":
    paces +=1
if decard == "A":
    daces +=1

phand2 = phand

print(f"""
----------------------------
         Welcome to:
        *Black Jack*

         by Kaspar
----------------------------
""")
t.sleep(1)
print(f"""
---------------------------------------------
The player got a:\n  {pcard1}""")
t.sleep(1)
print(f"and a:\n  {pcard2}")
t.sleep(1)
print(f"for a combined hand of:\n  {phand}")
t.sleep(1.5)
print(f"""The dealer shows you one of his cards:\n  {dcard2}
---------------------------------------------
""")
t.sleep(1)
try:
    # Player Hit and Stand loop
    while phand < 21:
        action = str(input("""press h to hit or s to stand
  """).lower())
        if action == "h":
            t.sleep(0.5)
            print("\nYou chose to hit\n")
            phand = phand + intpecard
            t.sleep(0.5)
            print(f"You got a\n  {pecard}")

            # Player: Bust and Aces if statement
            if phand > 21:
                if paces > 0:
                    paces -= 1
                    phand -= 10
                    t.sleep(1)
                    print("Your Ace turned into a 1")
                else:
                    pbust = True

            phand = phand
            t.sleep(1)
            print(f"your total is now\n  {phand}")
        elif action == "s":
                t.sleep(0.5)
                print(f"\nYou chose to stand\n")
                phand = phand
                break

    if pbust == False:
        t.sleep(2)
        print(f"The dealer flips over his hidden card:\n  {dcard1}")
        t.sleep(1)
        print(f"combined with his previous card:\n  {dcard2}")
        t.sleep(2)
        print(f"\nthe dealer has a hand of:\n  {dhand}\n")

    # Dealer draw loop
        while dhand < 17:
            dhand = dhand + intdecard
            t.sleep(1)
            print("The Dealer has under 17 and has to hit\n")
            t.sleep(1)
            print(f"Dealer got a\n  {decard}")
                # Dealer: Bust and Aces if statement
            if dhand > 21:
                if daces > 0:
                    daces -= 1
                    dhand -= 10
                    t.sleep(1)
                    print("The Dealers Ace turned into a 1")
                else:
                    dbust = True
            t.sleep(1)
            print(f"the dealers total is now\n  {dhand}")

except KeyboardInterrupt:
    end = True
    print("""
---------------------
Black Jack has ended.
---------------------
""")
t.sleep(2)
if end == False:
    if pbust == True:
        print(f"""
----------------------------------------------------------------
                You got over 21 and busted
                       *You lose*        
----------------------------------------------------------------
""") 

    elif dbust == True:
        print(f"""
----------------------------------------------------------------
            The dealer got over 21 and busted
                        *You win*
----------------------------------------------------------------
""") 

    elif phand > dhand:
        print(f"""
----------------------------------------------------------------
Your hand of {phand} is greater than the dealers hand of {dhand}
                        *You win*
----------------------------------------------------------------
""")

    elif dhand > phand:
        print(f"""
----------------------------------------------------------------
The dealers hand of {dhand} is greater than your hand of {phand}
                        *You lose*
----------------------------------------------------------------
""")

    elif phand == dhand:
        print(f"""
----------------------------------------------------------------
        Both you and the Dealer got a hand of {phand}
                        *Push*
----------------------------------------------------------------
""")
