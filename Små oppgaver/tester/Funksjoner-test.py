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

""" 
def text_uten_vokal(text):
    text = text.replace("a","").replace("e","").replace("o","").replace("i","").replace("y","").replace("æ","").replace("ø","").replace("å","")
    return text

text = text_uten_vokal(input(""))
print(text_uten_vokal(text))
"""

# Oppgave 2 Lag en funksjon kvadrat(tall) som returnerer tallet opphøyd i andre potens.
""" 
tall = int(input(""))

def kvadrat(tall):
    tall = tall**2
    return tall

print(kvadrat(tall))

 """
# Oppgave 2 løsnings forslag
""" 
def kvadrat(tall):
    return tall ** 2

print(kvadrat(4))  # 16
 """

# Oppgave 11 Lag en rekursiv funksjon summer_til(n) som regner ut summen av alle heltall fra 1 til og med n, 
# uten å bruke en løkke, sum() eller range().
""" 
svar = int(input(""))
def summer_til(n):
    svar = n
    svar = (n + 1)*n/2
    return int(svar)

print(summer_til(svar))
 """

# Oppgave 11 løsningsforslag
def summer_til(n):
    if n <= 0:              # basistilfelle
        return 0
    else:
        return n + summer_til(n - 1)  # rekursivt steg

print(summer_til(5))  # 15  (1+2+3+4+5)