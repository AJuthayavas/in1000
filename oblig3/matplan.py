#Oppretter tre ordbøker, med ulike navn og matmenyer #
Ole = {
"Pasient 1": "Ole",
"Frokost": "Egg & bacon",
"Lunsj": "Kylling salat",
"Middag": "Kjøttkaker i brunsaus",
}

Dole = {
"Pasient 2": "Dole",
"Frokost": "Vafler",
"Lunsj": "Hummersuppe",
"Middag": "Sushi",
}

Doffen = {
"Pasient 3": "Doffen",
"Frokost": "Pannekaker med lønnesyrup",
"Lunsj": "Fruktsalat & yoghurt",
"Middag": "Baby bbq ribs",
}

#Her har jeg laget en prosdyre for å kunne sjekke om pasienten eksisterer i systemet.#
def print_ordboka():
    print(Ole)
    print(Dole)
    print(Doffen)

    print("....................................................................................................")

    bruker = input("Skriv inn beboerens navn for å se dagens meny: ")

    if bruker == "Ole" or bruker == "ole":
        print(Ole)

    elif bruker == "Dole" or bruker == "dole":
        print(Dole)

    elif bruker == "Doffen" or bruker == "doffen":
        print(Doffen)

    else:
        print("Dette navnet er ikke registrert i databasen desverre, prøv igjen!")

print_ordboka()

"""
Spm1: Liste, fordi man kan man lete etter en spesifikk verdi lista gjennom index, som for eksempel navn.

Spm2: Ordbok, fordi hvert brukernavn kan lagre en "poengsum" og dermed passer ordbok bedre enn liste/mengde

Spm3: Mengde, fordi rekkefølgen på personene ikke har noenting å si

Spm4: Mengde, hvis det ikke er viktig å vite hvem som har allergi. Med tanke på fellesmat for alle gjestene.
Ordbok funker bedre hvis matretter blir laget individuelt for enhver person. Altså at rettene er "forhåndslaget" for gjestene.

"""
