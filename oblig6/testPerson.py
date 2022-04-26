#Importerer klasse fra en annen fil
from person import Person

#Oppretter et hovedprogram til å kjøre metodene
def hovedprogram():
    personUno = Person("Testbruker 1", 999)
    #personUno.leggTilHobby()
    print(".............................................................")
    personUno.skrivUt()
    #print(personUno.skrivHobbyer())

    #personDos.printo()


hovedprogram()
