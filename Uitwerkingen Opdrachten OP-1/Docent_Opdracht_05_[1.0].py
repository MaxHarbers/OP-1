
# Docent Python Tooling
# Opdracht 05
"""
Vraag aan de gebruiker de volgende informatie:

-	Naam van een artikel
-	Aantal dagen dat het in het magazijn heeft gelegen.

Het programma geeft vervolgens weer, in een passende zin, hoeveel uur het artikel in het magazijn heeft gelegen.

Alle invoer moet met input( ) worden gerealiseerd.
"""

# Gebruiker om invoer data vragen.
naam_artikel_invoer = input( "Naam van het artikel: " )

aantal_dagen_invoer = input( "Aantal dagen dat het artikel in het magazijn lag: " )

# Omrekenen dagen naar uren.
aantal_dagen = int(aantal_dagen_invoer)
aantal_uren = aantal_dagen * 24

# Weergeven berekende waarden.
print( "Artikel {0} ligt {1} uur in het magazijn.".format(naam_artikel_invoer, aantal_uren) )

