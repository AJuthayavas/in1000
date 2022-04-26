#Her har jeg opprettet en prosedyre som legger sammen to tall
def adder(x, y):
    return(x + y)

print("1 + 4 =", adder(1, 4))
print("2 + 7 =", adder(2, 7))

print("......................")

##################################################


#Her har jeg laget en input-felt som lar brukeren taste inn en setning.
#Deretter skal programmet mitt beregne antall tilfeller av et "x" tegn

minTekst = input("Skriv inn en setning her: ")
minBokstav = input("Se hvor mange ganger du har tastet denne bokstaven: ")

tellForekomst = 0

for i in minTekst:
    if i == minBokstav:
        tellForekomst = tellForekomst + 1

print("......................................................................................")
print("Du skrev:", minTekst, "og det er registerert", str(tellForekomst), "tilfeller av bokstaven:", minBokstav)




##################################################
