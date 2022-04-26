#Oppretter 3 funksjoner. Tester alle med 3 ulike asserts
print("Addisjon:")
def addisjon(x, y):
    return x + y

print(addisjon(1, 4))
print(addisjon(-1, 5))
print(addisjon(-1, -1))

assert addisjon(1, 4) == 5
assert addisjon(-1, 5) == 4
assert addisjon(-1, -1) == -2

print("......................")


print("Subtraksjon:")
def subtraksjon(x, y):
    return x - y

print(subtraksjon(10, 2))
print(subtraksjon(5, -1))
print(subtraksjon(-5, -5))

assert subtraksjon(10, 2) == 8
assert subtraksjon(5, -1) == 6
assert subtraksjon(-5, -5) == 0

print("......................")


print("Divisjon:")
def divisjon(x, y):
    return y / x

print(divisjon(10, 10))
print(divisjon(-1, 10))
print(divisjon(-1, -1))

assert divisjon(10, 10) == 1
assert divisjon(-1, 10) == -10
assert divisjon(-1, -1) == 1

print("......................")



############################################################################################



def tommerTilCm(antallTommer):
    assert antallTommer > 0, "Woops, kompis tallet ditt MÅ være større enn 0!"
    beregner = antallTommer*2.54
    return beregner

print("Gjør vi om f.eks 16 tommer til cm, så får vi:", tommerTilCm(16), "centimeter.")


print("......................")



############################################################################################



def skrivBeregninger():
    print("Nå skal du taste inn to tall!")
    uno = float(input("Første tall: "))
    dos = float(input("Andre tall: "))

    print("......................")

    print("Addisjon:", uno, "+", dos, "=", addisjon(uno, dos))
    print("Subtraksjon:", uno, "-", dos, "=", subtraksjon(uno, dos))
    print("Divisjon:", dos, "÷", uno, "=", divisjon(uno, dos))
    print("......................")

    print("Nå skal tommer konverteres til cm!")
    inches = float(input("Tast inn et tall i tommer her: "))
    print("Tommer til centimeter =", tommerTilCm(inches))

skrivBeregninger()



############################################################################################
