#Importerer klasse fra en annen fil
from hund import Hund

#Oppretter et hovedprogram til å kjøre metodene
def hovedprogram():

    #oppretter 2 objekter
    woof1 = Hund(7, 50, 10)
    woof2 = Hund(2, 33, 5)

    #Printer ut objektene via metodene
    print("<--Hund 1--->")
    print(woof1.hentInfo())
    print(".............................................................")
    print(woof1.spring())
    print(".............................................................")
    print(woof1.spis(25))

    print("\n")

    print("<--Hund 2--->")
    print(woof2.hentInfo())
    print(".............................................................")
    print(woof2.spring())
    print(".............................................................")
    print(woof2.spis(2))




hovedprogram()
