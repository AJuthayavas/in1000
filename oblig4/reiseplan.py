#Nå skal 3 lister opprettes hvor man kan legge til 5 elementer
steder = []
destinajon = 0

for i in range(0, 5):
    destinasjon = input("tast inn et reisemål her: ")
    steder.append(destinasjon)

print(steder)


print("...................................")


klesplagg = []
clothing = 0

for i in range(0, 5):
    clothing = input("tast inn et klesplagg her: ")
    klesplagg.append(clothing)

print(klesplagg)



print("...................................")


avreisedato = []
dato = 0

for i in range(0, 5):
    dato = input("tast inn avreisedato her (DD.MM.YYYY): ")
    avreisedato.append(dato)

print(avreisedato)


print("...................................")


#Legger til de tre øverste listene inni en ny liste. Deretter printes de ut til bruker.
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedato)

print(reiseplan)

for x in range(len(reiseplan)):
    print(reiseplan[x])



#####    print(reiseplan[0][2])   #####

"""

reiseplan = []

findItem = int(input("Hvilken liste vil du printe ut? "))
findItem2 = int(input("Hvilket element fra lista vil du printe ut? "))


if 0 <= findItem <= 2:
    print(findItem2)

else:
    print("Ugyldig input")
    print(findItem)

if findItem2 == 2:
    print(reiseplan[findItem2])




                while 2>= findItem <=0:
                    print("Listen du valgte eksisterer ikke!")
                    findItem = int(input("Hvilken liste vil du printe ut? "))

                    print(findItem2)


                    if 4>= findItem2 <=0:
                        print(reiseplan[findItem][findItem2])

                    else:
                        print("Elementet fra listen du valgte eksisterer ikke")
                        findItem2 = int(input("Hvilket element fra lista vil du printe ut? "))




"""
