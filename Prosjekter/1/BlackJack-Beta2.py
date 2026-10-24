import random as r
import time as t

#Dictianary for shoe-en
Card_values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}
shoe = []

for key in Card_values.keys():
    for k in range(0, 16):
        shoe.append(key)
r.shuffle(shoe)
print(shoe)

indeks = 0
chips = 100
maxbet_str: list = ["m", "max", "M", "Max", "maxbet"]

def Menu():
    print(f"""
----------------------------
         Welcome to:
        *Black Jack*

         by Kaspar
----------------------------
""")
    t.sleep(1)

def bet(bet):
    global chips
    print(f"You have {chips} chips")
    while fbet == False:
        bet = int(input("How many chips do you bet: "))
        try:
            if bet <= chips and bet > 0:
                chips = chips - bet
                print(chips)
                fbet = True
            else:
                print("Invalid")
                fbet = False            
        except ValueError:
            if bet == maxbet_str[0]:
                bet = chips
                chips = 0
                fbet = True
            else:
                print("Invalid")
                fbet = False
            
        

class Opponents:
    def __init__(self, name):
        self.name = name
        self.aces = 0
        self.bust = False
        self.hand = []
        self.inthand = []

    def draw(self):
        global indeks
        self.card = shoe[indeks]
        self.intcard = int(Card_values[shoe[indeks]])
        indeks += 1
        self.hand.append(self.card)
        self.inthand.append(self.intcard)

    def bustaces(self):
        if self.inthand > 21:
            if 1 == 1:
                1
Opponent = [Opponents("Player"), Opponents("Dealer")]
Player = Opponent[0]
Dealer = Opponent[1]

def starting_hand():
    for i in range(2):
        Player.draw()
        Dealer.draw()

    s_h_da = ()
    if Player.inthand == 22:
        Player.inthand.append(-10)
        Player.aces =- 1
        s_h_da = print("One of your Aces turned into a 1")
    if Dealer.inthand == 22:
        Dealer.inthand.append(-10)


    print(f"""
    ---------------------------------------------
    The Player got a:\n  {Player.hand[0]}""")
    t.sleep(1)
    print(f"and a:\n  {Player.hand[1]}")
    t.sleep(1)
    print(f"for a combined hand of:\n  {sum(Player.inthand)}")
    t.sleep(1.5)
    print(f"""The Dealer shows you one of his cards:\n  {Dealer.hand[1]}
    ---------------------------------------------
    """)
    t.sleep(1)

# The Game
# -------------------------------------------------------------------------
Menu()

while chips < 1000 and chips > 0:
    #bet()
    starting_hand()
    while sum(Player.inthand) < 21 and Player.aces == 0 or Player.aces == -1:
        action = input("""Press h to hit or s to stand
    """).lower()
        if action == "h":
            t.sleep(0.5)
            print("\nYou chose to hit\n")
            Player.draw()
            t.sleep(0.5)
            print(f"You got a\n  {Player.hand[-1]}")
            t.sleep(1)
            print(f"your total is now\n  {sum(Player.inthand)}")
        elif action == "s":
                t.sleep(0.5)
                print(f"\nYou chose to stand with your hand of {sum(Player.inthand)}\n")
                break
        




#sum([Card_values[self.hand] for card in self.hand])
