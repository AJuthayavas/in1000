#Oppgave 1.1 = Lag en fil ved navn ​variabler.py​. (svaret er bare navnet på dokumentet)#


#Oppgave 1.2 = Skriv et program i denne filen som skriver ut ”Hei Student!” til terminalen#
#Gjorde ikke no spesielt her, skrev bare inn koden for å printe ut en linje som sier "Hei student"#
print("Hei student!")


#Oppgave 1.3 = Endre programmet slik at du ber brukeren om å oppgi et navn i form av entekststreng#
#ved hjelp av funksjonen ​input()​, og lagre denne verdien i en variabelnavn​. Skriv så ut “Hei “ og variabelen ​navn​#
#Her lagde jeg en variabel som het navn, den skulle brukes i tillegg til en hilsen som sier "Halla"#
navn = input("Skriv inn navnet ditt her: ")
print( "Halla " + navn )


#Oppgave 1.4 + 1.5 = Utvid programmet ditt med to variabler. Du kan velge variabelnavn selv, men gibegge variablene#
#heltallsverdier. Skriv ut variablene på hver sin linje. Beregn differansen av de to variablene (den første minus#
#den andre) og leggresultatet inn i en ny variabel. Skriv ut “Differanse:” etterfulgt av denne tredjevariabelen#
#Her lagde jeg to variabler med en verdi, og den skulle regne ut forskjellen mellom dem#
tall1 = 5
tall2 = 3
Differanse = tall1 - tall2
print("5 - 3 blir", Differanse)


#Oppgave 1.6 = Be bruker om å oppgi et nytt navn, og legg svaret i en ny variabel. Lag nok envariabel ved navn ​sammen​,#
#og gi den verdien av det første navnet etterfulgt av detandre navnet. Skriv ut ​sammen ​på en ny linje#
#Opprettet en linje som skulle printe ut det første navnet og det andre#
#-----------------------------------------------------------------------------------------------------------------------#
#navn2 = input("Skriv inn navnet ditt på nytt her, helst etternavnet: ")
#print( "Halla på deg igjen " + navn )
#sammen = navn + navn2
#print(sammen)
#-----------------------------------------------------------------------------------------------------------------------#

#Oppgave 1.7 = Du skal nå endre verdien av variabelen ​sammen​. Dette skal du gjøre ved å slå sammen de to navnene som i#
#forrige deloppgave, men denne gangen skal du leggetil “og” med et mellomrom på hver side mellom dem. For eksempel:#
#Dersom ​sammenførst hadde verdien “OlaKari!” skal den nå ha verdien “Ola og Kari”#
#Her lagde jeg et mellomrom mellom navn1 og navn2 og la til et "og" imellom#
navn2 = input("Skriv inn navnet ditt på nytt her, helst etternavnet: ")
print( "Halla på deg igjen " + navn )
sammen = navn + " og " + navn2
print(sammen)
