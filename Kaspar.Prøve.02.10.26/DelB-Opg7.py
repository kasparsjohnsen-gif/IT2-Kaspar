""" 
a) Bruk en for-løkke til å skrive ut hver deltaker på formen Ada har 42 poeng. (1 poeng)

b) Regn ut og skriv ut hvor mange poeng deltakerne har til sammen, og hvem som vant. (1 poeng)

c) Spør brukeren om et navn. Finnes navnet, skal programmet skrive ut poengsummen. Finnes det ikke, 
skal programmet skrive ut Fant ingen deltaker med navnet ... i stedet for å krasje. (1 poeng)
"""
poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
# a)
for key in poeng:
    print(f"{key} har {poeng[key]} poeng")
# b)

print(f"Summen av poengene ble {sum(poeng.values())}", end=" ")

for navn, sortedpoeng in sorted(poeng.items(), key=lambda par: par[1], reverse=True):
    print(f"og {navn} fikk mest poeng")
    break
# c)

Navn = str(input("Skriv inn et navn: "))
if Navn in poeng:
    print(f"{Navn} fikk {poeng[Navn]}")
else:
    print(f' Det er ingen med navnet "{Navn}" i databasen')
