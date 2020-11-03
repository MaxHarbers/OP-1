# M. Harbers 1016640 ICTDT1A
# Opdracht 3
# Versie 1
# Een computersimulatie van een chemische plant kost 97.500,- euro
# voor het huren gedurende een periode van een jaar. Elk jaar wordt er
# een kostenverhoging van 6,75% doorgevoerd. Het programma mag niet herhalen.
# Schrijf een programma dat huurkosten na 30 jaar uitrekent.
# Het antwoord moet op het scherm getoond worden.

simulatieKosten = 97500.0
verhoging = 6.75
verhogingsPercentage = verhoging / 100.0

for jaar in range(30):
    verhogingJaar = simulatieKosten * verhogingsPercentage
    simulatieKosten = simulatieKosten + verhogingJaar
    print("Kosten in jaar {0}: euro {1:.2f}".format(jaar, simulatieKosten))

print("Huurkosten na 5 jaar euro {0:.2f}".format(simulatieKosten))