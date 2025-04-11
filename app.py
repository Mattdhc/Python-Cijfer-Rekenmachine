# Variabelen
error_vraag = "Error: Vraag niet (juist) beantwoord!"
error_negatief_nummer = "Error: Gewicht is negatief!"

# Functies
# Maakt een herhalings functie aan
def herhaal():
    global opnieuw_gewichten_berekenen
    if vraag_gewichten == "Ja" or "ja":
        opnieuw_gewichten_berekenen()  
    while True:
        herhaal()

def opnieuw_gewichten_berekenen():
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25
    vak_gewicht = float(input("Wat is uw " + vak + " gemiddelde "))
    totaal_gewicht = vak_gewicht + vorig_totaal_gewicht

    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? "))
    totaal_cijfer = vak_cijfer + vorig_totaal_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
        
    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        vorig_totaal_gewicht == totaal_gewicht
        vorig_totaal_cijfer == totaal_cijfer
        print(vorig_totaal_gewicht)
        print(vorig_totaal_cijfer)
        herhaal()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    else:
        print(error_vraag)

# Vraagt aan de gebruiker of hij/zij verschillende gewichten wilt gebruiken
vraag_gewichten = str(input("Wilt u gewichten per vak invullen? (Ja of Nee) "))

# Maakt een functie die het gemiddelde cijfer berekent met verschillende gewichten per vak
if vraag_gewichten == "Ja" or vraag_gewichten == "ja":
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25
    vak_gewicht = float(input("Wat is uw " + vak + " gemiddelde "))
    totaal_gewicht = vak_gewicht

    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? "))
    totaal_cijfer = vak_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
    print(round(gemiddelde_cijfer))

    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        vorig_totaal_gewicht = totaal_gewicht
        vorig_totaal_cijfer = totaal_cijfer
        print(vorig_totaal_gewicht)
        herhaal()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    else:
        print(error_vraag)

# Maakt een functie die het gemiddelde cijfer berekent 
if vraag_gewichten == "Nee" or vraag_gewichten == "nee":
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25
    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? "))
    totaal_cijfer = vak_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
    print(round(gemiddelde_cijfer))

    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        herhaal()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    else:
        print(error_vraag)
else:
    print(error_vraag)