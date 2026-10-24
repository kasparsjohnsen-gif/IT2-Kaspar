import random as rd
sult = 5
energi = 5
glede = 5
game = True
navn = "Mia"
list = [0,0,0,0,0,0,0,0,0,1]

def begrens(verdi):
    return max(0, min(10, verdi))

def mate():
    global sult, glede
    sult = begrens(sult - 3)
    glede = begrens(glede + 1)
    print(f"Du ga {navn} mat")

def leke():
    global glede, energi
    glede = begrens(glede + 3)
    energi = begrens(energi - 1)
    print(f"Du lekte med {navn}")

def sove():
    global energi, sult
    energi = begrens(energi + 4)
    sult = begrens(sult + 1)
    print(f"Du lot {navn} sove")

def good_boy():
    print(f"{navn} har lyst at du skal kalle henne for en good boy?")
    gb = input("""ja/nei
    :""").lower()
    while True:
        if gb == "ja":
            global glede
            glede = begrens(glede + 5)
            print(f"{navn} begynte å logre med halen og bjeffe")
            False
        elif gb == "nei":
            print(f"{navn} ble lei seg")
            global glede
            glede = begrens(glede - 5)
        else:
            print("""ugyldig svar,prøv på nytt
ja/nei
:""")
            True
        

def tiden_går():
    global sult, glede
    sult = begrens(sult + 1)
    glede = begrens(glede - 1)

print(f"Hei, mitt navn er {navn}, hva vil du at jeg skal gjøre")
while game == True:
    menu = input(f"""
{navn}: sult {sult}, energi {energi}, glede {glede}
1: Mate  2: Leke  3: Sove  0: Avslutt
Velg:""")
    if menu == "1":
        mate()
    elif menu == "2":
        leke()
    elif menu == "3":
        sove()
    elif menu == "0":
        break
    else:
        print("ugyldig input, prøv noe annet")
    
    tiden_går()

    rd.shuffel(list)
    if list[0] == 1:
        good_boy()
    else:
        continue



    if sult > 8 <10:
        print("Veldig sulten")
    elif sult == 10:
        print(f"{navn} døde av sult")
        break
    else:
        continue
    if energi < 2 > 0:
        print(f"{navn} er trøtt")
    elif energi == 0:
        print(f"{navn} er så trøt at hun begynte å sove")
        sove()
    else:
        continue

