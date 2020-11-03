
# Docent Python Tooling 
# Opdracht 03
"""
Schrijf een programma dat de kosten van de zakelijke directie telefoons berekent
met behulp van de volgende gegevens:

Telefoon Jacob per maand	Telefoon Fred per maand
Euro 45,-	abonnement	Euro 48.50	abonnement
Euro 35,-	verzekering	Euro 38,75	verzekering
Euro 15,-	bellen en SMS	Euro 15,-	bellen en SMS

Ze hebben een 2 jarig contract.

kostenJacob = optellen kosten van Jacob
kosten Fred = optellen kosten van Fred
totale maandkosten = kosten Jacob + kosten Fred
kosten contractduur = 2 * 12 * totale maandkosten

Geef de totale kosten weer in de onderstaande zin,
waarbij de x wordt vervangen door het berekende bedrag:

De totale kosten van de directie telefoons gedurende het contract bedraagt x euro.

"""

# Kostenberekening
kosten_Jacob = 45.0 + 35.0 + 15.0
kosten_Fred = 48.50 + 38.75 + 15.0
totale_maandkosten = kosten_Jacob + kosten_Fred
kosten_contractduur = 2 * 12 * totale_maandkosten

# Weergave van de kosten
print( "De totale kosten van de directie telefoons gedurende het contract bedraagt {0:.2f} euro.".format(kosten_contractduur ) )
