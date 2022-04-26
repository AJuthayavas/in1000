def minFunksjon():
  for x in range(2):
    c = 2
    print(c)
    c += 1
    b = 10
    b += a
    print(b)
    return (b)

def hovedprogram():
  a = 42
  b = 0
  print(b)
  b = a
  a = minFunksjon()
  print(b)
  print(a)


hovedprogram()


"""
Først defineres funksjonen «minFunksjon», og ingen parametere blir tatt imot.
Deretter opprettes det en prosedyre «hovedprogram». Så skal «hovedprogram»
printes ut. a blir tilgitt verdien 42, og b 0. Deretter printes b ut som 0.
Så sier prosedyren at b skal nå bli 42. Deretter skal a representere den
første funksjonen, «minFunksjon». Skjønte ikke helt hva «for x in range (2)»
skal utføre men ja. Vet i hvert fall i neste steg skal c få verdien 2, og
den blir også printet ut. Deretter legges til 1 i verdi c, slik at c blir
nå 3. Deretter skal b få tilgitt verdien 10, og den skal adderes med verdi
a. Og verdi a er ikke definert i funksjonen så jeg regner med at maskinen
ikke klarer å forstå dette. Regner med at på linje 8, så vil ikke b bli
printet ut på grunn av at a «ødelegger» koden.


Tydeligvis hadde jeg rett. Testet med pythontutor.com og den viser også at
kun 0 og 2, blir printet ut til brukeren. Deretter sier den at a ikke er
definert. Regner med at det er derfor b ikke kan printes ut til brukeren.
"""
