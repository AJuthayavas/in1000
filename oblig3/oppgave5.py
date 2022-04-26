"""

WOHOO!!! Invitasjon til AJ sin bursdagsfest!

I denne oppgaven skal du planlegge en bursdagsfest. Du skal lage et skjema hvor det er mulig å melde opp 5 gjester.
I tillegg må hver av gjestene oppgi allergi. Om gjestene har en allergi som ikke kan unngås på menyen, så skal de ikke inviteres.

Opprett først en ordbok med liste over 5 navn. Hver person må oppgi allergi.

Masse lykke til!
Hilsen admin!

"""

#Lager først en prosedyre, og oppretter en ordbok hvor man kan melde seg opp, og legge til en allergi#
def print_bursdag():
    print("Hei og velkommen til AJ sin bursdagsfest. Fyll ut navnet ditt her, og nevn allergier du har.")
    print("Om du har noen allergier som ikke kan unngås, så er du desverre ikke invitert på festen :(")

    print("\n")

    ordbok = {}

    navn1 = input("Fyll ut navnet ditt her: ")
    allergi1 = input("Har du en allergi? ")

    print("..................................")
    navn2 = input("Fyll ut navnet ditt her: ")
    allergi2 = input("Har du en allergi? ")

    print("..................................")

    navn3 = input("Fyll ut navnet ditt her: ")
    allergi3 = input("Har du en allergi? ")

    print("..................................")

    navn4 = input("Fyll ut navnet ditt her: ")
    allergi4 = input("Har du en allergi? ")

    print("..................................")

    navn5 = input("Fyll ut navnet ditt her: ")
    allergi5 = input("Har du en allergi? ")

    print("..................................")


    ordbok[navn1] = allergi1
    ordbok[navn2] = allergi2
    ordbok[navn3] = allergi3
    ordbok[navn4] = allergi4
    ordbok[navn5] = allergi5

    if allergi1 == "Ost" or allergi1 == "ost" or allergi1 == "Gluten" or allergi1 == "gluten" or allergi1 == "Hvete" or allergi1 == "hvete":
        print("Sorry", navn1, "men du har en allergi så du er ikke invitert på bursdagen desverre.")
    else:
        print("Supert", navn1, "du har ikke noen allergier som står i veien for matrettene på festen, så du er invitert.")

    print(".................................................................................")

    if allergi2 == "Ost" or allergi2 == "ost" or allergi2 == "Gluten" or allergi2 == "gluten" or allergi2 == "Hvete" or allergi2 == "hvete":
        print("Sorry", navn2, "men du har en allergi så du er ikke invitert på bursdagen desverre.")
    else:
        print("Supert", navn2, "du har ikke noen allergier som står i veien for matrettene på festen, så du er invitert.")

    print(".................................................................................")

    if allergi3 == "Ost" or allergi3 == "ost" or allergi3 == "Gluten" or allergi3 == "gluten" or allergi3 == "Hvete" or allergi3 == "hvete":
        print("Sorry", navn3, "men du har en allergi så du er ikke invitert på bursdagen desverre.")
    else:
        print("Supert", navn3, "du har ikke noen allergier som står i veien for matrettene på festen, så du er invitert.")

    print(".................................................................................")

    if allergi4 == "Ost" or allergi4 == "ost" or allergi4 == "Gluten" or allergi4 == "gluten" or allergi4 == "Hvete" or allergi4 == "hvete":
        print("Sorry", navn4, "men du har en allergi så du er ikke invitert på bursdagen desverre.")
    else:
        print("Supert", navn4, "du har ikke noen allergier som står i veien for matrettene på festen, så du er invitert.")

    print(".................................................................................")

    if allergi5 == "Ost" or allergi5 == "ost" or allergi5 == "Gluten" or allergi5 == "gluten" or allergi5 == "Hvete" or allergi5 == "hvete":
        print("Sorry", navn5, "men du har en allergi så du er ikke invitert på bursdagen desverre.")
    else:
        print("Supert", navn5, "du har ikke noen allergier som står i veien for matrettene på festen, så du er invitert.")

    print(".................................................................................")
    print(ordbok)


print_bursdag()
