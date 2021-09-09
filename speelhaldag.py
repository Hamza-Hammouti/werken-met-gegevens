toegangsticket = 7.45
gameseat = 0.074                 # De prijs van de gameseat is voor 1 minuut.
totaalaantalminuten = 45

toegangsticketaantal = 3
gameseataantal = 27

totaalprijs = toegangsticket * toegangsticketaantal + ((totaalaantalminuten * gameseat) * 3)

print("Dit geweldige dagje-uit met " + str(toegangsticketaantal) + " mensen in de Speelhal met " + str(totaalaantalminuten) + " minuten VR kost je maar " + str(totaalprijs)