#Starter med å lage en liste med tall, og deretter bruker jeg append kommandoen for å legge inn et tall jeg ønsker.#
myList = [17, 21, 777]
myList.append(999)
print ("Første tallet i lista er:", myList[0], "og det tredje tallet er:", myList[2])

print("..................................")

#Her oppretter jeg en ny tom liste, og nedenfor der igjen, har jeg laget 4 input-felt for brukeren til å taste inn navn selv#
liste2 = [];

liste2.append(input("Legg til ditt første navn her: "))
liste2.append(input("Legg til ditt andre navn her: "))
liste2.append(input("Legg til ditt tredje navn her: "))
liste2.append(input("Legg til ditt fjerde navn her: "))

print("..................................")

print("Her er de 4 navnene du tastet inn:", liste2)

print("..................................")

#Her har jeg laget en if-else test for å sjekke om brukeren har vært snill og lagt inn navnet mitt også#
if "AJ" in liste2 or "Aj" in liste2 or "aj" in liste2 or "Ajandth" in liste2 or "ajandth" in liste2 or "Admin" in liste2 or "admin" in liste2:
    print("Heyheyyy du huska navnet mitt jo ^-^")

else:
    print("Hallo? Du glemte navnet mitt jo?!?!")

print("..................................")

print("\n")

print("Tilfelle du glemte listen:", myList)

#Her har jeg laget en liten funksjon som ganger alle tallene inni listen#
plusse = sum(myList)
myList =[17, 21, 777, 999]
gange = 1

for x in myList:
    gange = gange * x

print("Dette får du hvis du plusser alle tallene sammen:", plusse)
print("Dette får du hvis du multipliserer alle tallene sammen:", gange)

#Her kager jeg en ny liste som kun inneholder plusse og gange#
newList = [plusse, gange]
print("Her er en ny liste med de to nye tallene du nettopp fikk:", newList)

print("..................................")

#Her er den fullstendige listen, altså 17, 21, 777, 999, 1814, 277111611#
endaEnNewList = (myList + newList)
print("Her er din nye fullstendige liste:", endaEnNewList)

print("..................................")

#Oppretter en funksjon for å slette de to siste tallene (plusse og gange).#
print("Nå skal de to siste tallene fjernes.")
del endaEnNewList[4:6]
print(endaEnNewList)

print("\n")
print("Uff, dette må nok være den mest hjernesprengende oppgaven jeg har gjort...")
