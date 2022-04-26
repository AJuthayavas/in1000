#Oppretter en tom ordbok, deretter en funksjon.
dictionary = {}

def les_fil_til_dict(filnavn):
    selve_filen = open(filnavn)

#Splitter hver linje in CSV filen der det finnes en komma.
#Deretter putter jeg dem i en ordbok, som jeg tidligere opprettet.
    for linje in selve_filen:
        individuell_linje = linje.split(" ")

        for elementer in individuell_linje:
            values = elementer.split(",")
            dictionary[values[0]] = float(values[1])

    selve_filen.close()
    return dictionary


execute = les_fil_til_dict("max_temperatures_per_month.csv")
print(execute)

print("......................")


############################################################################################

#Oppretter enda en funksjon som gjør det samme som i oppgaven ovenfor.
#Men denne gangen skal den sammenlikne 2 filer. Og printe ut en melding
def rekord(ordbok, file):
    maximumPerDag = open(file)

    for kolonne in maximumPerDag:
        content = kolonne.split(",")

        month = content[0]
        day = content[1]
        temperature = float(content[2])
        monthday = month+day

        rekordForHverMåned = ordbok[month]

        if temperature > rekordForHverMåned:
            rekordForHverMåned = temperature
            print("Programmet fant en ny varmerekord den", day, month, "og da var temperaturen", rekordForHverMåned, "°C.", "Den gamle rekorden lå på", ordbok[month], "°C.")

        #Deretter oppdaterer vi den nye ordboken
            ordbok[month] = rekordForHverMåned
    maximumPerDag.close()
    return ordbok

print(rekord(les_fil_til_dict("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv"))

print("......................")


############################################################################################

#Nå skal den nye ordboken puttes inn i en ny fil
def copy2NewFile(ordbok, newFile):
    file = open(newFile, "w")

    ordbok = rekord(ordbok, "max_daily_temperature_2018.csv")
    for i in ordbok:
        file.write(i + "," + str(ordbok[i]) + "\n")

    file.close()

copy2NewFile(les_fil_til_dict("max_temperatures_per_month.csv"), "ordbokUpdated.csv")

print("Oppdatert informasjon har blit puttet inn i en ny csv-fil.")
print("......................")


############################################################################################
