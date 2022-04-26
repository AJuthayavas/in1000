#Importerer klasse fra en annen fil
from dato import Dato

#Oppretter et hovedprogram til å kjøre metodene
def hovedprogram():
    dato1 = Dato(15, 12, 2001)
    print(dato1.skrivUtAar())
    dato1.sjekkDag() #Bruker return value i metoden, dermed
                     #trengs ikke print. Ellers printer den ut 15 i en ny linje
    dato1.streng() #Samme prinsipp som forrige line
    print("............................................")

hovedprogram()
