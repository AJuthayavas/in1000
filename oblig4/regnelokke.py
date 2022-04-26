#Starter med å lage en liste hvor man kan taste inn så mange elementer man vil, helt til man taster 0.
null = int(input("Bare å fyre seg løs med tilfeldige tall: "))

liste1 = []

while null != 0:
    liste1.append(null)
    print("Du skrev ikke 0")
    null = int(input("Bare å fyre seg løs med tilfeldige tall: "))

print("Riktig, du skrev endelig det tallet admin ville at du skulle (0).")

#Sortering part.1
print("......................")
print("En liste har blitt opprettet for å vise deg hva slags tall du har tastet inn, bare hyggelig :)")

print(liste1)

#Sortering part.2
print("......................")
print("Nå har tallene blitt printet ut separat, ved hjelp av en -for loop-, hvis du synes dette er mer ryddigere ellerno")

#Nå opprettes det en funksjon for å plusse sammen tall, finne laveste tallet og største tallet.
for x in range(len(liste1)):
    print(liste1[x])




minSum = 0
for null in range(0, len(liste1)):
    minSum += liste1[null]

print("Dette får du hvis du plusser alle tallene sammen:", minSum)


minst = liste1[0]
for e in liste1:
    if e < minst:
        minst = e

print("Dette er det minste tallet i liste:", minst)


stoerst = liste1[0]
for i in range(1, len(liste1)):
    if liste1[i] > stoerst:
        stoerst = liste1[i]

print("Det største tallet i lista er:", stoerst)
