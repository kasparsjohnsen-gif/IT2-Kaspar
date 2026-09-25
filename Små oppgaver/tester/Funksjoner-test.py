"""
liste_printet = False
def legg_til(element, liste=[]):

    if element == None:
        return liste
    liste.append(element)
    return liste

while liste_printet == False:
    addtion = input('Legg til noe i listen, når du er ferdig skriv "print"\n    ')
    if addtion == "print":
        print(legg_til(None))
        liste_printet = True
    else:
        legg_til(addtion)
        liste_printet = False
"""

# Lag en funksjon som tar en streng som parameter og returnerer en ny streng der alle vokalene er fjernet.

def text_uten_vokal(text):
    text = text.replace("a","").replace("e","").replace("o","").replace("i","").replace("y","").replace("æ","").replace("ø","").replace("å","")
    return text

text = text_uten_vokal(input(""))
print(text_uten_vokal(text))

