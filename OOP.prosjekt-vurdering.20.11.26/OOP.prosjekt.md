# **Your local shop**

## **Gameplay:**

## **Coreloop:**
Du driver en liten sjappe hvor du seller og kjøper ulike gjenstander for å kunne betale renten din.
Renten øker med hver dag som går helt til du ikke greier å betale den.
Hver dag vil det komme 3 personer på rad og gi deg ulike tilbud.
de ulike personene kan enten selle deg ting, kjøpe ting fra deg eller gi deg et tilbud.
Når du seller og kjøper kan du velge hvor mye du har lyst til å selge eller kjøpe med i håp om at personen velger å akseptere prisen du har valgt
Etter at du har "interacted" med hver av de tre personene vil det bli natt.
Om natten vil det komme en spøkelse og "curse" sjappen din med enten en slags curse

### **NPCs**
NPCene blir puttet i tre grupper:
**Merchants**: de har primert lyst til å selge deg noe.
**Costumers**: de vil primert kjøpe ting fra deg.
**Deal makers**: de vil bare gi deg en spesifikk deal som kan ha noe å si med pengene dine eller itemsene dine.

Sjansen for at du greier å overselle eller underpaye kommer an på persuasion staten din, prestige staten din og hvilke trait NPCen har

Traits er additional stats en NPC kan ha som sier noe om hvor lett og hvor mye du kan hagle med dem.

### **Items:**

**Itemstats**
Items har en base-sellvalue og en base-buyvalue.
Items kan også ha enten en pristige stat eller en persuasion stat.


**Raritys:**
commen, uncommen, rare, legendary

**Item classes:**
*Furniture*
*Clothing*
*Tools*
*Tech*
*Food*

**Liste av ulike items:**
**Commen items:**
*Old-Chair* 'Furniture' - Buy: 3g - sell: 2g

**Uncommen items:**
*SnowGlobe* 'Furniture' - Buy: 4g - sell: 2g - Info: Øker sell value med 1g per dag som går

**Rare items:**
*Fedora* 'Clothing' - Buy: 10g - sell: 6g - persuasion 25
*Life-sized SnowGlobe* 'Furniture' - Buy: 10g - sell: 6g - Info: Øker sell value med 3g per dag som går

**Legendary items:**
*Cactus* 'Furniture' - Buy: 20g - sell: 14g - prestige 50 - Info: 


# **Krav til spillet**
## Minst tre egne klasser, der hver klasse har attributter og metoder som hører naturlig til den.

Arv: Minst én klasse skal arve fra en annen klasse og bruke super(). Subklassen skal enten legge
til noe nytt eller overstyre minst én metode.

Objekter som samarbeider: Objektene skal bruke eller endre hverandre. For eksempel kan en spiller angripe en fiende, eller en bank kan ha mange kontoer.

Mange objekter samlet i en liste eller en dictionary, som programmet går gjennom med en løkke.

Brukerinput, for eksempel en meny der brukeren velger hva som skal skje.

Feilhåndtering: Programmet skal ikke krasje hvis brukeren skriver noe ugyldig.

Lesbar kode: gode navn på klasser, metoder og variabler, og kommentarer der det ikke er åpenbart hva koden gjør.

## I tillegg skal du lage:

Et klassediagram som viser klassene dine med attributter og metoder, og hvilke klasser som arver fra hverandre. Du kan tegne det på papir, i et tegneprogram eller i en README.md. Se eksempelet under.

En README.md i prosjektmappa di som
forklarer hva programmet gjør og hvordan det kjøres
hvilke kilder du har brukt (nettsider, eksempelkode og lignende)
hvordan du har brukt KI (se Bruk av KI)
en kort oppsummering av hva du har gjort, når (logg)


# **Logg** 
27.10.26
planlegging av spillet

# **Kilder**
## KI
### Claude
**05.11.2026**
Spurte Claude om en måte å kunne velge et tilfeldig navn fra en txtfil som jeg kunne bruke videre.
Dette var malen jeg fikk:
```
from pathlib import Path
import random

BASE_DIR = Path(__file__).parent
NAMES_FILE = BASE_DIR / "names.txt"

def load_names(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

names = load_names(NAMES_FILE)
name = random.choice(names)
```

## Venner/medelever
### Paul 
### Isak

