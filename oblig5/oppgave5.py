"""

I denne oppgaven skal man kunne lese inn en csv-fil via python. Deretter skal
informasjonen puttes i en ordbok slik at det blir oversiktlig å lese dette.
Så skal innholdsverdiene i ordboken bli omgjort fra tommer til centimeter.
Altså man skal opprette en funksjon som omgjør tall, også skal man kalle på
denne i en ny prosedyre.

"""

dictionary = {}

def les_fil_til_dict(filnavn):
    selve_filen = open(filnavn)

    for linje in selve_filen:
        individuell_linje = linje.split("  ")

        for elementer in individuell_linje:
            values = elementer.split(" ")
            dictionary[values[0]] = float(values[1])

    selve_filen.close()
    return dictionary


execute = les_fil_til_dict("maal.csv")
print(execute)

print("......................")

############################################################################################

def tommerTilCm(antallTommer):
    beregner = antallTommer*2.54
    return beregner

############################################################################################


def prosedyre():
    print("Nå skal tommer gjøres om til cm!")
    print("......................")

    for key in dictionary:
        print(dictionary[key], "tommer")

    print("......................")

    for value in dictionary:
        print(tommerTilCm(dictionary[value]), "cm")

prosedyre()


############################################################################################
