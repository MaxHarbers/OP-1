

# Docent Python Tooling
# Opdracht 11
"""
De directie wil weten wat de kosten zijn voor het huren van een opslagruimte.
De huur bedraagt 835,- euro per jaar en wordt elk jaar 1.75% verhoogd.

Schrijf een programma welke aan de gebruiker vraagt hoeveel jaar de opslagruimte wordt gehuurd.
Bereken vervolgens de totale kosten van de huur gedurende die periode.

Geef de kosten onder elkaar weer als in onderstaand voorbeeld:
Kosten huur jaar 1: x
Kosten huur jaar 2: y
...

Waarbij x het bedrag van het eerste jaar weergeeft, y het bedrag van het 2de jaar, etc.
"""

# Definieren van de constanten
huur = 835.0
stijgings_percentage = 1.75

# Vragen aan de gebruiker hoeveel jaren hij/zij wil huren
aantal_jaren_huur = int( input( "Voor hoeveel jaren  wilt u huren? > " ) )


# Bereken per jaar wat de kosten zijn
for jaar in range(aantal_jaren_huur):
    kosten = huur + (jaar * 835 * (stijgings_percentage / 100.0))
    print( "Kosten huur jaar {0}: {1:.2f}" .format(jaar + 1, kosten) )
