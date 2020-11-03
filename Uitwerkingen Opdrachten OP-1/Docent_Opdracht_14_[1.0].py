

# Docent Python Tooling
# Opdracht 14

'''
Wanneer een klant iets besteld moet er een bon worden opgemaakt.
Hierop staan de bestelde items met de aantallen, bedragen, factuurnummer en het afleveradres.
Maak een programma waarin 4 artikelen zijn besteld door meneer H. Obby, woonachtig op
Houtxperimentlaan 72, 6271 OK te Basiselek. Klantnummer: 83723,
Factuurnummer: FAC2017-9152.

Artikelen = ["Arduino Uno", "Ultrasonic Sensor - HC-SR04 (Generic)",
"Adafruit Standard LCD -16x2 White on Blue", "Resistor 220ohm", "Resistor 470ohm", "Jumper wires"]

Prijzen = [20.0, 4.78, 9.90, 0.05, 0.07, 2.45]

Artikelen weergeven, waarbij de aantallen van alles 1 is.
De kolom aantal bestaat uit 5 karakters en begint aan het begin van de regel.
Uitlijnen aan de rechterzijde van de aantal kolom.
De kolom artikel is 45 karakters breed en begint op karakter 7 vanaf het begin van de regel,
waarbij de uitlijning links is.
De prijs kolom is 10 karakters breed en begint op karakter 47, waarbij de uitlijning rechts is.
Voeg als laatste regel de berekende totaalprijs toe, welke in de prijs kolom moet worden
weergegeven. Eveneens rechts uitgelijnd.
Geef de bon weer op het scherm.
'''

Artikelen = ["Arduino Uno", "Ultrasonic Sensor - HC-SR04 (Generic)", "Adafruit Standard LCD -16x2 White on Blue", "Resistor 220ohm", "Resistor 470ohm", "Jumper wires"]
Prijzen = [20.0, 4.78, 9.90, 0.05, 0.07, 2.45]

print( )
print( "{0:<7}| {1:<45}|{2:>10}".format("Aantal", "Artikel", "Prijs") )
print( 65 * "-" )
for artikel, prijs in zip(Artikelen, Prijzen):
    aantal = "{0:>7}| ".format("1")
    artikelNaam = "{0:<45}|".format(artikel)
    prijs = "{0:>10}".format(prijs)

    print( "{0}{1}{2}".format(aantal, artikelNaam, prijs) )
print( 65 * "-" )
print( "{0:>54}|{1:>10}" .format("Totaal", sum(Prijzen)) )
