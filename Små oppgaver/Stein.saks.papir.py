import random


playerpoint: int = 0
cpupoint: int = 0
draw: int = 0

print(f"""
---------------------------------------

Velkommen til stein, saks, papir!
laget av Kaspar

---------------------------------------

""")

while playerpoint < 3 and cpupoint < 3:
    playerchoice = str(input("""
    
    Skriv enten stein, saks eller papir: 
    
    """))
    cpuchoice = str(random.choice(["stein", "saks", "papir"]))

    #stein choices
    if playerchoice == "stein" and cpuchoice == "stein":
        draw += 1
        print("Begge valgte stein. Det ble uavgjort")

    elif playerchoice == "stein" and cpuchoice == "papir":
        cpupoint += 1
        print("Du valgte stein, mens cpu-en valgte papir. Cpu-en fikk poeng")

    elif playerchoice == "stein" and cpuchoice == "saks":
        playerpoint += 1
        print("Du valgte stein, mens cpu-en valgte saks. Du fikk poeng")

    #saks choices
    elif playerchoice == "saks" and cpuchoice == "saks":
        draw += 1
        print("Begge valgte saks. Det ble uavgjort")

    elif playerchoice == "saks" and cpuchoice == "stein":
        cpupoint += 1
        print("Du valgte saks, mens cpu-en valgte stein. Cpu-en fikk poeng")

    elif playerchoice == "saks" and cpuchoice == "papir":
        playerpoint += 1
        print("Du valgte saks, mens cpu-en valgte papir. Du fikk poeng")

    #papir choices
    elif playerchoice == "papir" and cpuchoice == "papir":
        draw += 1
        print("Begge valgte papir. Det ble uavgjort")
    
    elif playerchoice == "papir" and cpuchoice == "saks":
        cpupoint += 1
        print("Du valgte papir, mens cpu-en valgte saks. Cpu-en fikk poeng")
    
    elif playerchoice == "papir" and cpuchoice == "stein":
        playerpoint += 1
        print("Du valgte papir, mens cpu-en valgte stein. Du fikk poeng")

if playerpoint == 3:
    print(f"""
    ---------------------------------------------------------------------------------------------------
    Du fikk 3 poeng og vant spillet! Cpu-en fikk {cpupoint} poeng, og dere hadde uavgjort {draw} ganger
    ---------------------------------------------------------------------------------------------------
    """)
else:
    print(f"""
    ----------------------------------------------------------------------------------------------------------
    Cpu-en fikk 3 poeng og du tapte spillet! Du fikk {playerpoint} poeng, og dere hadde uavgjort {draw} ganger
    ----------------------------------------------------------------------------------------------------------
    """)