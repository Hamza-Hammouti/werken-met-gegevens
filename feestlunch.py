croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

croissantaantal = 17
stokbroodaantal = 2
kortingsbonaantal = 3

totaalprijs = croissant * croissantaantal + stokbrood * stokbroodaantal - kortingsbon * kortingsbonaantal

print("De feestlunch kost je bij de bakker " + str(totaalprijs) + " euro voor de " + str(croissantaantal) +" croissantjes en de " + str(stokbroodaantal) + " stokbroden als de " + str(kortingsbonaantal) + " kortingsbonnen nog geldig zijn!")