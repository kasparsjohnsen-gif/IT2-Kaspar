
alder = int(input("Hvor gammel er du?: "))
student = input("Er du student ja / nei?: ").lower()

if alder < 0 or alder > 120:
    print("Ugyldig tall for alder")
elif alder < 12:
    print("Biletten koster 80 kr")
elif alder >= 67:
    print("Biletten koster 100 kr")
elif 12 <= alder <= 30 and student == "ja":
    print("Biletten koster 110 kr")
else:
    print("Biletten koster 150 kr")