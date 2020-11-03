
# Docent Python Tooling 
# Opdracht 02
"""
Schrijf een programma dat de variabelen uit de vorige opdracht weergeeft in onderstaande zinnen:

De gebruikte schijfruimte op de server bedraagt { 1 } bytes.
De naam van de computer bij de receptie is: { 2 }.
De gemiddelde prijs van de verkochte Arduino boards is: { 3 } euro.
Wij garanderen een maximale levertijd van { 4 } dagen.

Waarbij de { x } moet worden vervangen door de waarde van de variabele met het coressponderende nummer uit opdracht 1.

"""

# Schijfruimte in bytes
schijfruimte = 107210362880

# Naam van de computer
pc_receptie = "DESKTOP_RECEPTIE"

# Prijs van het artikel
prijs_Arduino = 25.15

# Maximale aantal dagen
maximale_levertijd = 3

# Weergave op het scherm
print( )
print( "De gebruikte schuifruimte op de server bedraagt" ,schijfruimte, "bytes." )
print( ) 
print( "De gebruikte schijfruimte op de server bedraagt %i bytes." % schijfruimte )
print( )
print( "De gebruikte schijfruimte op de server bedraagt {0} bytes.".format(schijfruimte) )
print( )
print( "De naam van de computer bij de receptie is: {0}.".format(pc_receptie ) )
print( )
print( "De gemiddelde prijs van de verkochte Arduino boards is: {0:.2f} euro.".format(prijs_Arduino ) )
print( )
print( "Wij garanderen een maximale levertijd van {0} dagen.".format(maximale_levertijd ) )  
print( )
print( "Alle variabelen door elkaar: {0} \n {1} \n \n \n{2} \n {3} \n {2} \n {1} \n {2} " .format(schijfruimte, pc_receptie, prijs_Arduino, maximale_levertijd) )



