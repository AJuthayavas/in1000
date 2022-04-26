#Oppretter en tom ordbok
#Fornavnet og førstebokstav i etternavnet skal lagres som et brukernavn
#lower funksjonen er for å gjøre om store tegn til små
dictionary = {}

def lagBrukernavn(user):
    smaaBokstaver = user.lower()
    smaaBokstaverSplittes = smaaBokstaver.split(" ")
    userName = smaaBokstaverSplittes[0] + smaaBokstaverSplittes[1][0]

    return userName

user = input("Tast inn navnet ditt her: ")
print("Her er brukernavnet ditt: " + lagBrukernavn(user))



print("......................")


############################################################################################


#Oppretter en ny funksjon for å slå sammen et brukernavn, alfakrøll og en suffix
suffix = "student.matnat.uio.no"
user = lagBrukernavn(user)

def lagEpost(user, suffix):
    epost = user + "@" + suffix

    return epost


print("Eposten din blir: " + lagEpost(user, suffix))


print("......................")


############################################################################################

#Funksjonen skal printe ut epostadresser ved hjelp av infoen i ordboken.
dictionary = {"userx": "ifi.uio.no", "usery": "student.matnat.uio.no"}

def printEposter(dictionary):

    for i in dictionary:
        epostCreate = lagEpost(i, dictionary[i])

        print(epostCreate)

    return epostCreate


printEposter(dictionary)


print("......................")


############################################################################################

statement = "xXx"

while statement != "s":
    statement = input("Tast inn enten i/p/s. [i = opprett en epost] // [p = print epost fra ordbok] // [s = avslutt programmet]: ")

    if statement == "i":
        fullName = input("Tast inn fornavnet og etternavnet ditt her: ")
        suffix = input("Tast inn et suffix her (ex; xmail.com): ")
        brukerNavn = lagBrukernavn(fullName)
        dictionary[brukerNavn] = suffix
        print(dictionary)

    elif statement == "p":
        printEposter(dictionary)

    elif statement == "s":
        statement = "s"

    else:
        statement = input("Tast inn enten i/p/s. [i = opprett en epost] // [p = print epost fra ordbok] // [s = avslutt programmet]: ")

quit()


############################################################################################
