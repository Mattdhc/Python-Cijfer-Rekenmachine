# (Error) Variabelen
error_vraag = "Error: Vraag niet (juist) beantwoord!"

# Functies
# Functie om gemiddelde te berekenen als de gebruiker om een nog een cijfer toe te voegen met gewichten
def opnieuw_gewichten_berekenen():
    global vorig_totaal_gewicht
    global vorig_totaal_cijfer
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25
    vak_gewicht = float(input("Wat is uw " + vak + " gemiddelde ? "))
    totaal_gewicht = vak_gewicht + vorig_totaal_gewicht
    vorig_totaal_gewicht = totaal_gewicht

    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? ")) * vak_gewicht
    totaal_cijfer = vak_cijfer + vorig_totaal_cijfer
    vorig_totaal_cijfer = totaal_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
    print("uw gemiddelde is:", round(gemiddelde_cijfer, 1))
      
    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        opnieuw_gewichten_berekenen()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    if nogeencijfer != "Ja" or not "ja" or not "Nee" or not "nee":
        print(error_vraag)

# Functie om gemiddelde te berekenen als de gebruiker om een nog een cijfer toe te voegen
def opnieuw_cijfers_berekenen():
    global vorig_totaal_gewicht
    global vorig_totaal_cijfer
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25
    totaal_gewicht = 1 + vorig_totaal_gewicht
    vorig_totaal_gewicht = totaal_gewicht

    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? "))
    totaal_cijfer = vak_cijfer + vorig_totaal_cijfer
    vorig_totaal_cijfer = totaal_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
    print("uw gemiddelde is:", round(gemiddelde_cijfer, 1))
      
    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        opnieuw_cijfers_berekenen()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    if nogeencijfer != "Ja" or not "ja" or not "Nee" or not "nee":
        print(error_vraag)

# Vraagt aan de gebruiker of hij/zij verschillende gewichten wilt gebruiken
vraag_gewichten = str(input("Wilt u gewichten per vak invullen? (Ja of Nee) "))

# Start het programma die het gemiddelde cijfer berekent met verschillende gewichten per vak
if vraag_gewichten == "Ja" or vraag_gewichten == "ja":
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25
    vak_gewicht = float(input("Wat is uw " + vak + " gemiddelde "))
    totaal_gewicht = vak_gewicht
    vorig_totaal_gewicht = totaal_gewicht

    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? ")) * vak_gewicht
    totaal_cijfer = vak_cijfer
    vorig_totaal_cijfer = totaal_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
    print("uw gemiddelde is:", round(gemiddelde_cijfer, 1))

    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        opnieuw_gewichten_berekenen()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    if nogeencijfer != "Ja" or not "ja" or not "Nee" or not "nee":
        print(error_vraag)

# Start het programma die het gemiddelde cijfer berekent 
if vraag_gewichten == "Nee" or vraag_gewichten == "nee":
    vak = input("Wat is het vak waarvan uw het gemiddelde wilt berekenen? ")
    globals()[vak] = 25

    totaal_gewicht = 1
    vorig_totaal_gewicht = totaal_gewicht

    vak_cijfer = float(input("Wat is uw " + vak + " cijfer? "))
    totaal_cijfer = vak_cijfer
    vorig_totaal_cijfer = totaal_cijfer

    gemiddelde_cijfer = totaal_cijfer / totaal_gewicht
    print(round(gemiddelde_cijfer))

    nogeencijfer = str(input("Nog een cijfer berekenen? (Ja of Nee) "))
    if nogeencijfer == "Ja" or nogeencijfer == "ja":
        opnieuw_cijfers_berekenen()
    if nogeencijfer == "Nee" or nogeencijfer == "nee":
        exit()
    if nogeencijfer != "Ja" or not "ja" or not "Nee" or not "nee":
        print(error_vraag)

if vraag_gewichten != "Ja" or not "ja" or not "Nee" or not "nee":
    print(error_vraag)
