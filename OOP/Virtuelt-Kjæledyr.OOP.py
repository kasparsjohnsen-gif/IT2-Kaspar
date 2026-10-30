

def begrens(verdi):
    return max(0, min(10, verdi))

class Kjaeledyr:
    def __init__(self, navn):
        self.navn = navn
        self.sult = 5
        self.energi = 5
        self.glede = 5
        self.alder = 0

    def vis_status(self):
        print(f"{self.navn}: sult {self.sult}, energi {self.energi}, glede {self.glede}, alder {self.alder}")
        if self.sult >= 8:
            print(f"{self.navn} er sulten!")
        if self.energi <= 2:
            print(f"{self.navn} er trøtt!")

    def mate(self):
        self.sult = begrens(self.sult - 3)
        self.glede = begrens(self.glede + 1)
        print(f"Du ga {self.navn} mat.")

    def leke(self):
        self.glede = begrens(self.glede + 3)
        self.energi = begrens(self.energi - 1)
        print(f"Du lekte med {self.navn}")

    def sove(self):
        self.energi = begrens(self.energi + 4)
        self.sult = begrens(self.sult + 1)
        print(f"Du lot {self.navn} sove")

    def good_boy(self):
        print(f"{self.navn} har lyst at du skal kalle henne for en good boy?")
        gb = input("""ja/nei
:""").lower()
        while True:
            if gb == "ja":
                self.glede = begrens(self.glede + 5)
                print(f"{self.navn} begynte å logre med halen og bjeffe")
                False
            elif gb == "nei":
                print(f"{self.navn} ble lei seg")
                self.glede = begrens(self.glede - 5)
            else:
                print("""ugyldig svar,prøv på nytt
        ja/nei
        :""")
                True

    def bade(self):
        self.glede = begrens(self.glede - 1)
        self.energi = begrens(self.energi - 1)

    def tiden_går(self):
        self.sult = begrens(self.sult + 1)
        self.glede = begrens(self.glede - 1)
        self.alder = self.alder + 1


def velg_dyr(dyrene):
    for i, dyr in enumerate(dyrene):
        print(f"{i + 1}: {dyr.navn}")
    try:
        return dyrene[int(input("Hvilket dyr? ")) - 1]
    except (ValueError, IndexError):
        print("Ugyldig dyr.")
        return None


dyrene = [Kjaeledyr("Mia"), Kjaeledyr("Jesper")]

while True:
    print()
    for dyr in dyrene:
        dyr.vis_status()
    print("1: Mate  2: Leke  3: Sove  4: Adopter nytt dyr  0: Avslutt")
    valg = input("Velg: ")

    if valg == "0":
        break
    elif valg == "4":
        dyrene.append(Kjaeledyr(input("Navn på det nye dyret: ")))
    elif valg in ["1", "2", "3"]:
        dyr = velg_dyr(dyrene)
        if dyr is None:
            continue
        if valg == "1":
            dyr.mate()
        elif valg == "2":
            dyr.leke()
        elif valg == "3":
            dyr.sove()
        elif valg == "4":
            dyr.bade()
    else:
        print("Ugyldig valg.")
        continue

    for dyr in dyrene:
        dyr.tiden_går()

