import random
import time

playerpoint: int = 0
cpupoint: int = 0
draw: int = 0

print(f"""
---------------------------------------

        Velkommen til Spillet:
         stein, saks, papir!

           Laget av Kaspar

        Målet er å få 3 poeng, 
       før Cpu-en får 3 poeng

              Lykke til!
                 ; )
---------------------------------------
""")
time.sleep(1)

while playerpoint < 3 and cpupoint < 3:
    time.sleep(1)
    playerchoice = str(input("""
Skriv enten stein(1), saks(2) eller papir(3): 

    """).lower())

    if playerchoice == "1":
        playerchoice = "stein"
    if playerchoice == "2":
        playerchoice = "saks"
    if playerchoice == "3":
        playerchoice = "papir"

    messageD = str(random.choice(['"Great minds think alike"', '"IMPOSSIBLE"', '"Jeg viste ikke at dere begge var så dumme"', '"#TWINS!"', f'"Hvordan visste den at du skulle velge {playerchoice}?"']))
    messageW = str(random.choice(['"Nice"', '"Too easy!"', '"Bra jobbet"', f'"{playerchoice} on top!"', f'"Jeg visste at {playerchoice} var et bra valg"']))
    messageL = str(random.choice(['"Yikes"', '"Yup, du burde bare gi opp"', '"Du kan ikke vinne hver gang"', '"Hold ut! Du kan fortsatt ha et comeback!"', f'"Hvorfor valgte du {playerchoice}, Jeg visste at det var et dumt valg!"']))

    cpuchoice = str(random.choice(["stein", "saks", "papir"]))

    time.sleep(0.5)

    print(f"""
-------------------
Du valgte {playerchoice}""")
    time.sleep(1)
    print(f"""
Cpu-en valgte {cpuchoice}
-------------------""")

    time.sleep(1)

    #stein choices
    if playerchoice == "stein" and cpuchoice == "stein":
        draw += 1
        print("""
----------------
Det ble uavgjort
----------------
""")
        time.sleep(0.5)
        print(messageD)

    elif playerchoice == "stein" and cpuchoice == "papir":
        cpupoint += 1
        print("""
-----------------
Cpu-en fikk poeng
-----------------
""")

        time.sleep(1)
        print(messageL)

    elif playerchoice == "stein" and cpuchoice == "saks":
        playerpoint += 1
        print("""
-------------
Du fikk poeng
-------------
""")

        time.sleep(1)
        print(messageW)

    #saks choices
    elif playerchoice == "saks" and cpuchoice == "saks":
        draw += 1
        print("""
----------------
Det ble uavgjort
----------------
""")

        time.sleep(1)
        print(messageD)

    elif playerchoice == "saks" and cpuchoice == "stein":
        cpupoint += 1
        print("""
-----------------
Cpu-en fikk poeng
-----------------
""")

        time.sleep(1)
        print(messageL)

    elif playerchoice == "saks" and cpuchoice == "papir":
        playerpoint += 1
        print("""
-------------
Du fikk poeng
-------------
""")

        time.sleep(1)
        print(messageW)

    #papir choices
    elif playerchoice == "papir" and cpuchoice == "papir":
        draw += 1
        print("""
----------------
Det ble uavgjort
----------------
""")

        time.sleep(1)
        print(messageD)

    elif playerchoice == "papir" and cpuchoice == "saks":
        cpupoint += 1
        print("""
-----------------
Cpu-en fikk poeng
-----------------
""")

        time.sleep(1)
        print(messageL)

    elif playerchoice == "papir" and cpuchoice == "stein":
        playerpoint += 1
        print("""
-------------
Du fikk poeng
-------------
""")

        time.sleep(1)
        print(messageW)

    else:
        cpupoint += 1
        print(f'''
-----------------
Cpu-en fikk poeng
-----------------

Bro Hvorfor valgte du {playerchoice}? Fornøyd nå eller? Idiot!
''')
time.sleep(0.5)

messageVic = str(random.choice(['"Du er Geiten av stein, saks, papir"', '"Du knuste den clankeren"', '"Flott, nå er du klar for å redde menneskeheten"', '"Er stein, saks papir livet ditt eller?"']))
messageDef = str(random.choice(['"Du er trash"', '"Menneskeheten er cooked"', '"You disappoint me"', '"Hvoran tapte du mot en clancker?"']))

if playerpoint == 3:
    print(f"""
    --------------------------------------------------------------------------------------
    Du fikk 3 poeng og vant spillet! Cpu-en fikk {cpupoint} poeng, og dere hadde uavgjort {draw} ganger
    --------------------------------------------------------------------------------------
    """)
    print(f"""{messageVic}
""")


else:
    print(f"""
    ---------------------------------------------------------------------------------------------
    Cpu-en fikk 3 poeng og du tapte spillet! Du fikk {playerpoint} poeng, og dere hadde uavgjort {draw} ganger
    ---------------------------------------------------------------------------------------------
    """)
    print(f"""{messageDef}
""")