"""

I denne oppgaven skal du lage et program som tar inn navn og bursdagsdato.
Deretter skal du også lafe et inputfelt for å sjekke om personen eksisterer
i databasen. Om personen eksister skal man klare å printe ut når den personen
har bursdag!

"""


liste1 = []
navn = 0

for i in range(0, 3):
    navn = input("Tast inn navnet ditt her: ")
    liste1.append(navn)

print(liste1)


print("...................................................")

liste2 = []
bursdag = 0

for i in range(0, 3):
    bursdag = input("Tast inn bursdagen din her (DD.MM.YYYY): ")
    liste2.append(bursdag)

print(liste2)


print("...................................................")


testNavn = input("Velg et navn du vil sjekke ligger i databasen: ")


print("...................................................")


if testNavn in liste1:
    print("Navnet finnes i databasen!")

else:
    print("Navnet finnes desverre ikke i databasen!")


print("\n")




if testNavn == liste1[0]:
    print(liste1[0], liste2[0])

else:
    print("Navnet finnes ikke")


print("...................................................")


if  testNavn == liste1[1]:
        print(liste1[1], liste2[1])
else:
    print("Navnet finnes ikke")


print("...................................................")


if testNavn == liste1[2]:
    print(liste1[2], liste2[2])

else:
    print("Navnet finnes ikke")


"""

Den siste delen ble rar. Den tar med alle if-statementene. Den skal kun ta med
en if-statement, så ja.

"""
