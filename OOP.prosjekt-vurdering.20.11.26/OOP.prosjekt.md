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

### Chat-GPT
Spurte Chat om den kunne lage flere objekter jeg kunne ha I items classen:
'''
Commen_Items = [
    # Food
    Item("Half-Eaten Sandwich", "Commen", "Food", 5, 3, "Someone took a bite and decided they weren't hungry anymore"),
    Item("Expired Energy Drink", "Commen", "Food", 6, 3, "Probably expired three months ago, but it still has some fizz"),
    Item("Instant Noodles", "Commen", "Food", 4, 3, "A college student's favourite meal"),
    Item("Slightly Rotten Banana", "Commen", "Food", 3, 2, "It's mostly brown, but hey, it's still edible"),

    # Tech
    Item("Old Nokia Phone", "Commen", "Tech", 8, 6, "Survived a nuclear apocalypse, but can't run YouTube"),
    Item("Broken Headphones", "Commen", "Tech", 5, 3, "Only one side works, but that's better than nothing"),
    Item("USB Stick", "Commen", "Tech", 7, 5, "Contains 2GB of questionable files"),
    Item("Wired Mouse", "Commen", "Tech", 6, 4, "A perfectly normal computer mouse"),

    # Gear
    Item("Rusty Compass", "Commen", "Gear", 7, 5, "Points north... most of the time"),
    Item("Old Backpack", "Commen", "Gear", 9, 7, "Smells weird, but has plenty of storage"),
    Item("Wooden Walking Stick", "Commen", "Gear", 5, 4, "Perfect for old people and adventurers"),
    Item("Cheap Sunglasses", "Commen", "Gear", 6, 4, "Makes you look 10% cooler"),

    # Furniture
    Item("Old Wooden Chair", "Commen", "Furniture", 5, 4, "Your mothers Old Wooden Chair"),
    Item("Plastic Garden Chair", "Commen", "Furniture", 6, 4, "A classic chair found in every garden"),
    Item("Small Wooden Table", "Commen", "Furniture", 9, 7, "Nothing special, but it gets the job done"),
    Item("Old Bookshelf", "Commen", "Furniture", 8, 5, "Filled with books nobody has read"),

    # Clothing
    Item("Baseball Cap", "Commen", "Clothing", 7, 6, "Just a stylish Baseball Cap", persuasion=1),
    Item("Dirty White T-Shirt", "Commen", "Clothing", 5, 3, "Was white once, probably"),
    Item("Old Jeans", "Commen", "Clothing", 8, 6, "A little worn out, but still fashionable"),
    Item("Woolly Socks", "Commen", "Clothing", 4, 3, "Keeps your feet warm, what more could you ask for?")
]

Uncommen_Items = [
    # Your original items
    Item("Yamasks Mask", "Uncommen", "Clothing", 10, 8, "Found in a dumpster outside a therapy clinic", prestige=10),
    Item("Spagetti bolognese", "Uncommen", "Food", 10, 10, "Made by your local chef, tastes wonderfull", persuasion=3, abilities=Item.shrinking_value, params=(1,), abilities_info="Looses 1 gold resell value every day"),

    # Food
    Item("Homemade Apple Pie", "Uncommen", "Food", 14, 11, "Freshly baked by someone's grandmother", persuasion=4),
    Item("Expensive Cheese", "Uncommen", "Food", 16, 13, "A piece of imported cheese that apparently tastes amazing"),

    # Tech
    Item("Mechanical Keyboard", "Uncommen", "Tech", 17, 14, "Sounds like a machine when typing", persuasion=5),
    Item("Vintage Game Console", "Uncommen", "Tech", 16, 13, "An old gaming console that's still in pretty good condition", prestige=8),

    # Gear
    Item("Leather Backpack", "Uncommen", "Gear", 15, 12, "A well-made backpack with plenty of storage", prestige=5),
    Item("Silver Pocket Watch", "Uncommen", "Gear", 18, 15, "An old pocket watch that still works perfectly", prestige=8),

    # Furniture
    Item("Antique Wooden Cabinet", "Uncommen", "Furniture", 16, 13, "An old cabinet in surprisingly good condition", prestige=8),
    Item("Comfortable Recliner", "Uncommen", "Furniture", 14, 11, "A very comfortable chair that practically swallows you"),

    # Clothing
    Item("Designer Hoodie", "Uncommen", "Clothing", 18, 15, "A popular hoodie from a fairly expensive brand", persuasion=8),
    Item("Leather Jacket", "Uncommen", "Clothing", 17, 14, "A classic leather jacket that never goes out of style", prestige=7)
]

Rare_Items = [
    # Your original items
    Item("Fedora", "Rare", "Clothing", 15, 12, "Worn by a beaver, a cool beaver", persuasion=15),
    Item("Oled Monitor", "Rare", "Tech", 20, 15, "Once you go Oled you can never go back", prestige=25),

    # Food
    Item("Aged Wine Cheese", "Rare", "Food", 25, 21, "Aged for several years and sold at a surprisingly high price", persuasion=12),
    Item("Imported Truffle", "Rare", "Food", 28, 23, "A rare ingredient used by expensive restaurants"),

    # Tech
    Item("High-End Gaming PC", "Rare", "Tech", 30, 25, "A powerful gaming PC with some of the best components available", prestige=18),
    Item("Prototype Smartphone", "Rare", "Tech", 27, 22, "An unreleased phone that somehow ended up on the market", abilities=Item.growing_value, params=(2,), abilities_info="Gain 2 gold resell value every day"),

    # Gear
    Item("Professional Camera", "Rare", "Gear", 25, 21, "A professional camera used by experienced photographers", prestige=15),
    Item("Gold Pocket Watch", "Rare", "Gear", 29, 24, "A beautifully crafted pocket watch made from real gold", prestige=18),

    # Furniture
    Item("Handcrafted Dining Table", "Rare", "Furniture", 28, 23, "A large dining table made from expensive wood", prestige=15),
    Item("Antique Grandfather Clock", "Rare", "Furniture", 30, 25, "An old grandfather clock that still keeps perfect time", abilities=Item.passive_income, params=(2,), abilities_info="Generates 2 gold every day"),

    # Clothing
    Item("Limited Edition Sneakers", "Rare", "Clothing", 29, 24, "A limited release pair of sneakers that collectors really want", persuasion=18),
    Item("Expensive Business Suit", "Rare", "Clothing", 27, 22, "A professionally tailored suit worn by successful businessmen", prestige=15, persuasion=8)
]
'''

## Patorjk
[Link](https://patorjk.com/software/taag/#p=display&f=Slant&t=Your%0ALocal%0AShop&x=none&v=4&h=4&w=80&we=false)

## Venner/medelever



