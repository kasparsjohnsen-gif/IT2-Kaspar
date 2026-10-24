gyldig = False

while not gyldig:

    try:
        antall_biletter = int(input("Hvor mange billeter vil du kjøpe?: "))
        if 1 <= antall_biletter <= 10:
            pris = antall_biletter * 150
            print(f"Totalpris: {pris} kr")
            gyldig = True
        else:
            print("Du kan kjøpe mellom 1 og 10 billetter")
        
    except ValueError:
        print("Du må skrive inn et heltall")