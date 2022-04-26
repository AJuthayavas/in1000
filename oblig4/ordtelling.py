#Jeg har opprettet et program som teller antall bokstaver i et ord.
counterrr = {}

example = "Python"

for i in example.split():
    counterrr[i] = len(i)

print("Ordet er: Python, og det finnes", counterrr[i], "bokstaver i dette ordet.")


print("...................................................")


#Her printes det ut et setning, og den teller antall ord i setningen.
liste1 = "Halla sjef jeg driver å spiser ost jeg"
setning = liste1.split()

temp = set(setning)
result = {}
for e in temp:
    result[e] = setning.count(e)

print(setning)
print("Dette var setningen: ", liste1)
print("Antall ord i setningen du tastet inn =", result)


print("...................................................")


#Her skal brukeren oppgi en setning, den skal telle antall ord i setningen, og
#hvor mange ganger ordet gjentas i setningen. Deretter santall bokstaver i hvert ord.
userInput = input("Skriv inn en setning her: ")
antallOrdIstringen = len(userInput.split())
tredjeBeregning = userInput.split()



print("...................................................")
print("Dette er setningen din:", userInput)
print("Antall ord i setningen du tastet inn =", str(antallOrdIstringen))

ord = set(tredjeBeregning)
resultat = {}
for e in ord:
    resultat[e] = tredjeBeregning.count(e)
print("Antall ganger ordene blir gjentatt i setningen:", resultat)


count = {}
for x in userInput.split():
    count[x] = len(x)
print("Antall bokstaver per ord:", count)
