


# Docent Python Tooling
# Opdracht 12

"""
Opdracht 12
Nieuwe artikelnummers genereren komt elke keer terug in het systeem van Nohtyp.
Hier moeten we een robuuste functie voor maken. Daarnaast moet een artikelnummer
behalve een cijfer ook letters bevatten. Een artikelnummer wordt als volgt opgebouwd:
4 cijfers gevolgd door een minteken, 3 kleine letters gevolgd door een minteken,
3 kleine letters gevolgd door een minteken en als laatste 4 cijfers.

Bijvoorbeeld: 1234-abc-def-5678

Maak een functie die bij elke aanroep een nieuw artikelnummer teruggeeft in het formaat zoals
hiervoor is beschreven. Geef de functie een passende naam.

Genereer een lijst met 10 artikelnummers die door de functie worden gegenereerd en geef deze onder elkaar weer.
"""

import string
import random


def artikelnummers_genereren():

        cijfers_01 = random.randrange(999, 10000)
        cijfers_02 = random.randrange(999,10000)
        letters_01 = ''
        
        for y in range( 6 ):
                letters_01 += (random.choice(string.ascii_lowercase) )
                print( letters_01)

        print( "{0}-{1}-{2}-{3}".format( cijfers_01, ( letters_01 [:3 ] ), ( letters_01 [3:] ), cijfers_02 ) )


for x in range (10 ):
    artikelnummers_genereren()


