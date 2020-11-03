
# Docent Python Tooling
# Opdracht 10 1e oplossing

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

for i in range(1, 101):

    print( i)
    print ("Artikelnummer ", str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)) + ", ", end = '' )
    print ("Artikelnummer ", str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)) + ", ", end = '' )
    print ("Artikelnummer ", str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)))
    
    
