
# Docent Python Tooling 
# Opdracht 04
"""
Klanten kunnen ook in maandelijkse termijnen betalen. Als jaarrente rekenen wij 11.2%.
Bereken wat de maandrente bedraagt voor de klanten, gegeven de volgende formule:
   maandrente= ((1 + jaarrente / 100)^(1 / 12)) - 1

Geef het antwoord weer in onderstaande zin, waarbij x wordt vervangen door de berekende maandrente met 3 decimalen
achter de komma en y wordt vervangen door 11.2:
De maandrente bedraagt x% bij een jaarrente van y%.

"""
import math

# Opbreken van de formule in losse stukken.

jaar_rente_percentage = 11.2

jaar_rente = jaar_rente_percentage / 100.0

maand_macht = 1.0 / 12.0

jaar_waarde = 1.0 + jaar_rente

macht_verheffen = math.pow(jaar_waarde, maand_macht)

maand_rente = macht_verheffen - 1.0

maand_rente_percentage = maand_rente * 100.0

# Weergeven van de berekende maandrente.

print( "De maandrente bedraagt {0:.3f}% bij een jaarrente van {1}%.".format( maand_rente_percentage, jaar_rente_percentage) )


