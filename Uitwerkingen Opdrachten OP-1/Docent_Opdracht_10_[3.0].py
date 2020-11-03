

# Docent Python Tooling
# Opdracht 10 3e oplossing

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

# Genereren van 300 artikelnummers
for artikel in range(300):
    regel_met_nummers = "Artikelnummer "

    # Kolom weergave
    for kolom in range(3):
        eerste_cijfers = random.randint(100, 999)
        regel_met_nummers = "{0}{1}-".format(regel_met_nummers, eerste_cijfers)
        tweede_cijfers = random.randint(10, 99)
        regel_met_nummers = "{0}{1}".format(regel_met_nummers, tweede_cijfers)

        # Bepalen of er nog een kolom komt
        if kolom < 2:
            # Toevoegen ", Artikelnummer " voor de volgende kolom
            regel_met_nummers = "{0}, Artikelnummer ".format(regel_met_nummers)

    # Weergeven regel met artikelnummers
    print( regel_met_nummers )
    
