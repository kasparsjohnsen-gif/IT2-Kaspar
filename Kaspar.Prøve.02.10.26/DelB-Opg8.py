""" 
a) Lag en funksjon konverter_tid(sekunder) som tar inn et antall sekunder og returnerer hvor mange timer, minutter og sekunder det tilsvarer (tre returverdier). Kall funksjonen med 4000, og skriv ut resultatet på formen 1 t, 6 min, 40 s. (2 poeng)

b) Lag en funksjon er_sterkt_passord(passord) som returnerer True hvis passordet oppfyller alle kravene under, og False ellers: (2 poeng)

minst 8 tegn langt
inneholder minst ett siffer
inneholder minst én stor bokstav
Test funksjonen med disse tre passordene som viser at den fungerer: "hemmelig", "Hemmelig" og "Hemmelig1".

Tips: tegn.isdigit() gir True hvis tegn er et siffer, og tegn.isupper() gir True hvis tegn er en stor bokstav.

Bruk gjerne type hints på funksjonene dine.
"""

""" 
sekunder = int(input(""))

timer = sekunder // 3600
sekunder % 3600 == sekunder
minutter = sekunder // 60
sekunder % 60 == sekunder
print(f"{timer}t, {minutter}m, {sekunder}s")
 """

t = 64 % 60
print(t)


    
