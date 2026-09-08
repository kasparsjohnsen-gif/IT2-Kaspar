import random
import time

#Dictianary
values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}

shoe = []

for key in values.keys():
    for k in range(0, 16):
        shoe.append(key)

random.shuffle(shoe)

print(shoe)
# Player's and Dealer's card in str
pcard1 = shoe.pop(0)
dcard1 = shoe.pop(0)
pcard2 = shoe.pop(0)
dcard2 = shoe.pop(0)

# Player's and Dealer's card in int
intpcard1 = int(values[pcard1])
intdcard1 = int(values[dcard1])
intpcard2 = int(values[pcard2])
intdcard2 = int(values[dcard2])

paces = 0
daces = 0
phand = intpcard1 + intpcard2
dhand = intdcard1 + intdcard2
pbust = False
dbust = False

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

phand2 = phand

print(f"""
---------------------------------------------
The player got a:
{pcard1} 
and a: 
{pcard2}
for a combined hand of:
{phand}

The dealer shows you one of his cards: 
{dcard2}
---------------------------------------------
""")

# Player Hit and Stand loop
while phand < 21:
    action = str(input("""press h to hit or s to stand
    """).lower())
    if action == "h":
        ecard = shoe.pop(0)
        intecard = int(values[ecard])
        phand = phand + intecard
        phand = phand
        print(f"""You got a 
{ecard} 
your total is now 
{phand}""")
    elif action == "s":
            phand = phand
            break

# Player: Bust and Aces if statement
if phand > 21:
    if paces > 0:
        paces -= 1
        phand -= 10
    else:
        pbust = True

else:
    print(f"""The dealer flips over his hidden card: 
{dcard1}
combined with his previous card: 
{dcard2} 
the dealer has a hand of: 
{dhand}
""")

# Dealer draw loop
    while dhand < 17:
        ecard = shoe.pop(0)
        intecard = int(values[ecard])
        dhand = dhand + intecard
        print(f"Dealer got a {ecard}, the dealers total is now {dhand}")

# Dealer: Bust and Aces if statement
        if dhand > 21:
            if daces > 0:
                daces -= 1
                dhand -= 10
            else:
                dbust = True


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