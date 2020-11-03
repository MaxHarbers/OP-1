

# Docent Python Tooling
# Opdracht 10 2e oplossing

"""
Er wordt een partij nieuwe artikelen verwacht, daarbij zijn nieuwe artikelnummers nodig.

Schrijf een programma dat 300 willekeurige artikelnummers genereert.
Elk artikel heeft een nummer bestaande uit een willekeurig getal bestaande uit 3 cijfers en een
willekeurig getal van 2 cijfers gescheiden door een min teken (-).
Voeg de getallen samen en geef de artikelnummers weer.
Op elke regel worden er 3 artikelnummers weergegeven gescheiden door een komma.
Achter het laatste artikelnummer wordt geen komma weergegeven. Zie onderstaande als voorbeeld:

Artikelnummer 748-69, Artikelnummer 910-38, Artikelnummer 726-81
Artikelnummer 102-93, Artikelnummer 373-61, ...
"""

import random

aantalklaar = 0

while aantalklaar < 100:
    deel_1 = random.randrange(99,1000)
    deel_2 = random.randrange(10,100)
    deel_3 = random.randrange(99,1000)
    deel_4 = random.randrange(10,100)
    deel_5 = random.randrange(99,1000)
    deel_6 = random.randrange(10,100)

    print("Artikelnummer {0}-{1}, Artikelnummer {2}-{3}, Artikelnummer {4}-{5}".format(deel_1, deel_2, deel_3, deel_4, deel_5, deel_6))
    aantalklaar += 1
    
