
# Docent Python Tooling
# Opdracht 09
"""
Opdracht 9
De artikelen die van de leverancier worden geleverd en in het magazijn moeten worden opgeslagen moeten worden ingevoerd.
Schrijf een programma dat aan de gebruiker de volgende vragen stelt:

- Artikelnummer, minstens 5 cijfers en geen letters
- Naam van het artikel
- Prijs van het artikel

Het programma blijft vragen voor nieuwe artikelen totdat de gebruiker artikelnummer 0 invoert.

Het programma geeft het laatste compleet ingevoerde artikel weer.
"""


niet_klaar = True

while niet_klaar:
    # Vraag gebruiker om een artikelnummer
    artikel_nummer_invoer = int( input( "\nGeef een artikelnummer [0 voor einde] > " ) )
        
    # Bepalen of de gebruiker wilde stoppen
    if artikel_nummer_invoer == 0:
        niet_klaar = False
    else:
        # Bepalen of het artikelnummer minstens 5 cijfers heeft
        if artikel_nummer_invoer <= 9999:
            print( "Het artikelnummer bestaat minder dan 5 cijfers" )
        else:
            # Verdere informatie vragen
            artikel_naam_invoer = input( "Geef de naam van het artikel > " )
            artikel_prijs_invoer = input( "Geef de prijs van het artikel > " )
            artikel_prijs = float( artikel_prijs_invoer )

            # Resultaat weergeven
            weergave = "Nummer: {0}\nNaam: {1}\nPrijs: {2:.2f} euro".format(artikel_nummer_invoer, artikel_naam_invoer, artikel_prijs )
            print( weergave, )
            
