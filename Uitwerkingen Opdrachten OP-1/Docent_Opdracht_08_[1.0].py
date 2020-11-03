
# Docent Python Tooling
# Opdracht 08
"""
Een manager moet voor een nieuwe medewerker toegang regelen tot bepaalde bestanden
en printers doormiddel van een aanvraagformulier.
Schrijf een programma dat deze flowchart implementeert.
Geef bij elke stap op het scherm weer wat er gebeurt.
Bij de beslissingen wordt de vraag aan de gebruiker gesteld.
"""

print( "Formulier voor de manager die voor een nieuwe medewerker toegang aanvraagd \ntot bepaalde bestanden en printers.\n" )

# Naam van de nieuwe medewerker vragen

achternaam = input( "1. Wat is de achternaam van de nieuwe medewerker? " )

afdeling = input( "\n2. Op welke afdeling gaat deze medewerker werken? \nSales, ICT of Human Resouces? \nTyp Sales, ICT of Human Resouces. > ")


while not ( afdeling == "Sales"  or afdeling == "ICT" or afdeling == "Human Resources" ):
    afdeling = (input( "\nUw invoer is niet juist. \n2. Op welke afdeling gaat deze medewerker werken? \nSales, ICT of Human Resouces. \nTyp Sales, ICT of Human Resources. > " ) )
    
  
print( "\n3. Welke verantwoording? " )

if afdeling == "Sales" :
    verantwoording = input( "Marketing of Customer Care. \nType Marketing of Custom Care > " )  
    while not ( verantwoording == "Marketing" or verantwoording == "Custom Care" ):
        verantwoording = (input( "\nUw invoer is niet juist. \n3. Welke verantwoording? \nMarketing of Customer Care. \nTyp Marketing of Custom Care > " ) ) 


elif afdeling == "ICT" :
    verantwoording = input( "DevOps of Security. \nType DevOps of Security > ")
    while not ( verantwoording == "DevOps" or verantwoording == "Security" ):
        verantwoording = (input ( "\nUw invoer is niet juist. \n3. Welke verantwoording? \nDevOps of Security. \nTyp DevOps of Security > " ) )

        
elif afdeling == "Human Resources" :
    verantwoording = input( "Assistant of Manager. Type Assstant of Manager > ")
    while not ( verantwoording == "Assistant" or verantwoording == "Manager" ):
        verantwoording = (input( "\nUw invoer is niet juist. \n3 Welke verantwoording? \nAssistant of Manager. Typ Assistent of Manager > " ) )

        
print("\nDe naam van de nieuwe medewerker is {0}. \nHij of zij gaat op de afdeling {1} werken. \nEn heeft de verantwoording over {2}."  .format( achternaam, afdeling, verantwoording, ) )

