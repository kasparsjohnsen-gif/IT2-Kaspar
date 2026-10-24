# Først og fremst blir svaret i inputen en string og ikke en int
# Dette gjør at når programmet skal sjekke om alderen er under eller lik 18 eller om alderen er 17
# vil den ikke finne en int valuen sånn som er sagt i if-statementen at trengs for å oppflylle, 
# men etter en str som ikke er definert i koden.
# og da for man en TypeError

# Neste feil er at det mangler en kolon i linje 3 etter 18.
# Kolonen sier når selve linjen som sier hva som oppfyller if statmenten er ferdig.
# uten kolonen tror den at alder må være under eller lik 18 og print("Du er myndig") må bli oppfylt.
# Noe som ikke er mulig. Man for en SyntaxError.

# Siste feil er også en SyntaxError og skyldes at det på linje fem bare er et erlikhets tegn (=)
# mellom alder og 17.

# Oppdatert versjon:
alder = int(input("Hvor gammel er du? "))

if alder >= 18:
    print("Du er myndig.")
elif alder == 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")