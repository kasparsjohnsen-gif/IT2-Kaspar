""" 
a) Skriv ut hvor mange målinger det er, og hva den første og den siste målingen var. 
Bruk indeksering. (1 poeng)

b) Regn ut og skriv ut gjennomsnittstemperaturen, avrundet til én desimal. (1 poeng)

c) Bruk en løkke til å telle hvor mange dager temperaturen var under 0 grader, 
og skriv ut svaret. (1 poeng)

d) Lag en ny liste som bare inneholder temperaturene som var over 0 grader, 
sortert fra varmest til kaldest. Skriv ut den nye lista. 
Den opprinnelige lista skal ikke endres. (1 poeng)
"""
# a)
temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]
print(f"Det var {len(temperaturer)} målinger og den første temperaturen var {temperaturer[0]} grader, og den siste var {temperaturer[9]} grader")
# b)
gjennomsnitt = sum(temperaturer) / len(temperaturer)
print(f"Gjennomsnitts-temperaturen var {round(gjennomsnitt, 1)} grader")
# c)
antall_dager_under_0_grader = 0
for i in range(len(temperaturer)):
    if temperaturer[i] < 0:
        antall_dager_under_0_grader += 1
print(f"Det er {antall_dager_under_0_grader} dager hvor temperaturen var under 0 grader")
# d)
sortert_temperatur = sorted(temperaturer)
sortert_temperatur.sort(reverse=True)
print(f"{sortert_temperatur[:5]}")
