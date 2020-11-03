

# Docent Python Tooling
# Opdracht 13

"""
In opdracht 12 is een functie gemaakt die een artikelnummer genereerd
volgens een voorgeschreven formaat.
Stop deze functie in een module genaamd artikel.
Om ondanks de unieke artikelnummers toch een bepaalde structuur te kunnen
krijgen wil de directie met behulp van de eerste 3 letters in het artikelnummer
het soort artikel classificeren.
Daartoe zijn er 4 klassen bedacht: microcontroller, mini-PC, home automation, accessoires.

Breidt de module uit met een functie die de klasse teug geeft op basis van de eerste
3 letters van het artikelnummer.

Classificatie eerste letter van de eerste lettercombinatie:
 microcontroller a, b, c, d, e of f    97 98 99 100 101 102
 mini-PC g, h, i, j, k of l
 home automation m, n, o, p, q of r
 accessoires s, t, u, v, w, x, y of z

Maak in het hoofdprogramma een lijst met 10 artikelnummers.

Geef de artikelnummers onder elkaar weer, waarbij achter elk artikelnummer
de classificatie wordt weergegeven.

Bijvoorbeeld:
1234-abc-def-5678 microcontroller
9101-map-hjk-8219 home automation
"""


import artikel_02

for artikelnummers in range( 0, 100):
    artikel_02.artikelnummers_genereren( )
