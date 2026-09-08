t = str(input("Skriv in noe: "))

for i in t:
    print(i, end="#")

n = 0
for i in range(5):
    n+=1 
    print(f"Denne løkka har gjentatt seg {n} ganger.")