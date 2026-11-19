# **Your local shop**

## **Gameplay:**

## **Coreloop:**
Du driver en liten sjappe hvor du seller og kjøper ulike gjenstander for å kunne betale renten din.

Du starter med 10 gold og renten øker med hver dag som går helt til du ikke greier å betale den mer. Spillet slutter når du ikke har nok penger til å tilbake renten,

Hver dag vil det komme 3 personer til sjappen din en etter en og gi deg ulike tilbud.
Personen kan enten være en Merchant, Costumers, Buisnessman.
Når du seller og kjøper ulike items kan du velge hvor mye du har lyst til å selge eller kjøpe den for, i håp om at personen velger å akseptere prisen du har valgt.
Man kan øke denne sjansen ved å ha ulike items som øker prestige og persusajon i inventoryet sitt.
Etter at du har "interacted" med hver av de tre personene vil det bli kveld og du må betale renten før det blir neste dag.

### **NPCs**
NPCene blir puttet i tre grupper:
**Merchants**: de har lyst til å selge deg noe.
**Costumers**: de vil kjøpe ting fra deg.
**Buisnessman**: de vil bare gi deg en spesifikk deal som kan ha noe å si med pengene dine eller itemsene dine.

prestige øker sjansen din for å overselle
persuasion øker sjansen din for å underbuye

### **Items:**

**Itemstats**
Alle items har en base-sellvalue og en base-buyvalue.
Items kan også ha en prestige stat eller en persuasion stat.
I tillegg er det noen Items som har abilities

**Raritys:**
commen, uncommen, rare, legendary
commen 50% sjanse
uncommen 30% sjanse
rare 15 % sjanse
legendary 5% sjanse

**Item classes:**
*Furniture*
*Clothing*
*Gear*
*Tech*
*Food*

**Liste av ulike items(utdatert):**

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


