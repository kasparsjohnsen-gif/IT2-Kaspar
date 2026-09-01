"""

dag = 3

match dag:
    case 1:
        print("Måndag")
    case 2:
        print("Tysdag")
    case 3:
        print("Onsdag")
    case _:
        print("Ukjend dag")

alder = 17

match alder:
    case n if n < 0:
        print("Ugyldig alder")
    case n if n < 18:
        print("Du er mindreårig")
    case n if n < 67:
        print("Du er vaksen")
    case _:
        print("Du er pensjonist")


punkt = (0, 5)

match punkt:
    case (0, 0):
        print("Origo")
    case (0, y):
        print(f"På y-aksen, y = {y}")
    case (x, 0):
        print(f"På x-aksen, x = {x}")
    case (x, y):
        print(f"Vanleg punkt: ({x}, {y})")

"""

tall = int(input("skriv in et tall 1-12: "))

match tall:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("Apr")
    case 5:
        print("Mai")
    case 6:
        print("Juni")
    case 7:
        print("July")
    case 8:
        print("Aug")
    case 9:
        print("Sep")
    case 10:
        print("Okt")
    case 11:
        print("Nov")
    case 12:
        print("Des")
    