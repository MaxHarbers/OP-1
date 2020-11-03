
# Docent Python Tooling
# Opdracht 07
"""
Onderstaand wordt een flowchart weergegeven van een zeer eenvoudige firewall.
Zet deze flowchart om in een Python programma, waarbij je de teksten met de print() functie weergeeft.
Bij de beslissingsmomenten vraag je aan de gebruiker een ja/nee antwoord.
Afhankelijk van het door de gebruiker gegeven antwoord, vervolg je het bijbehorende pad.
"""


print( "Lees het netwerkbericht. \n" )

# Vragen is het doel bekend?

doel_bekend = input( "Is het doel bekend? Type ja of nee > " )

if doel_bekend == "ja" :
    print( "Pas filter regels toe. " )

    netwerk_bericht = input( "Is het netwerkbericht ok? Type ja of nee > ")
    if netwerk_bericht == "ja":
        print( "Stuur bericht door." )
        
    else:
        print( "Log netwerkbericht." )

else:
    print( "\nBericht laten vervallen." )

print( "\nEinde" )    

