
# Docent Python Tooling
# Opdracht 06
"""
Vraag aan de klant zijn / haar naam. Vervolgens vraag je de klacht die de klant wil indienen.
Het programma geeft vervolgens de volgende tekst weer,
waarbij x wordt vervangen door de ingevoerde naam en y door de ingevoerde klacht:

Geachte x,
Het spijt ons dat y is voorgekomen.
Wij doen onze best om dit zo spoedig mogelijk te herstellen.

Hoogachtend,

Team Nohtyp

Alle invoer moet met input( ) worden gerealiseerd.
"""

# Gebruiker om invoer data vragen.
naam_klant_invoer = input( "Naam van de klant: " )
klacht_klant_invoer = input( "Klacht omschrijving: " )

# Weergeven info.
print( )
print( "Geachte {0},".format(naam_klant_invoer) )

print( "Het spijt ons dat {0} is voorgekomen.".format( klacht_klant_invoer ) )

print( "Wij doen onze best om dit zo spoedig mogelijk te herstellen." )

print( "\nHoogachtend," )

print( "\nTeam Nohtyp" )
