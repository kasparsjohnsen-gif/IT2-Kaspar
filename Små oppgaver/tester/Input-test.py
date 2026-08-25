"""
tall1 = input("Skriv et tall ")
tall1 = float(tall1) 

tall2 = input("Skriv et tall ")
tall2 = float(tall2)

sum = tall1 + tall2

if sum % 1 == 0:
    sum = int(sum) 
#sjekker om sum er et heltall ved å dele summen på 1 og se etter rest
#hvis den ikke oppdager rest blir summen om til en int

print("Summen av tallene er", sum)
"""

C = input("Skriv in temperatur i celsius ")
C = float(C)

F = round((C*9/5) + 32, 2)

if F % 1 == 0:
    F = int(F)

if C % 1 == 0:
    C = int(C)


print(f"Temperaturen {C} grader i celsius er {F} grader i farenheit")


