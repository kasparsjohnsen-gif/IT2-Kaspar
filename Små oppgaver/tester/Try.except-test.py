"""
frukter = ["eple", "banan", "pære", "kiwi"]
gyldig = False

try:
    while not gyldig:
        indeks = input(f"Velg en frukt (0-{len(frukter) - 1}): ")

        try:
            indeks = int(indeks)
            valgt_frukt = frukter[indeks]
            gyldig = True
        except ValueError:
            print("Du må skrive inn et heltall.")
        except IndexError:
            print("Det finnes ingen frukt på den plassen.")
except KeyboardInterrupt:
    print("\nProgrammet ble avbrutt av brukeren.")
else:
    print(f"Du valgte {valgt_frukt}.")
"""

liste = list(range(1,12))
gyldig = False


try:
    while not gyldig:
        tall = int(input("skriv et tall fra 0 til 10: "))

        try:
            if tall >= 0:
                tall = (liste[tall]) - 1
                gyldig = True
            else:
                print("Har du lese kapasiteten til en tredje klassing?\nJeg sa: ET TALL FRA 0 til 10")

        except IndexError:
            print ("Har du lese kapasiteten til en tredje klassing?\nJeg sa: ET TALL FRA 0 til 10")
        except ValueError:
            print("Bro, det der er ikke et tall engang *crying emoji*")


except KeyboardInterrupt:
    print("\nGratulere, du skjønnte hvordan å stoppe koden.")

print(f" Ditt tall er {tall}")