'''
navn = "Jo Bjørnar Hausnes"
domene = "@skule.no"
epost = navn.replace(" ",".").lower().replace("ø","o")
print(epost)


filnavn = "Joe Bjørnars - Dans, Dans, Dans.mp3"
filtype = filnavn[-3:]
print(filtype)
'''

text = input("Skriv in tekst: ")

text2 = text.replace(" ","").lower()

text3 = text2[::-1]

if text3 == text2:
    print(f"teksten:({text}) er en palindrom")
else:
    print(f"teksten:({text}) er ikke en palindrom")