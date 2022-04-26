#Importerer klasse fra en annen fil
from motorsykkel import Motorsykkel

#Oppretter et hovedprogram til å kjøre metodene
def hovedprogram():

    #oppretter 3 objekter
    objekt1 = Motorsykkel("Yokohama", "AJ 777", 111)
    objekt2 = Motorsykkel("Ducati", "KH 7612", 725)
    objekt3 = Motorsykkel("Harley-Davidson", "CR 9623", 15)

    #Printer så ut disse 3 objektene
    print(objekt1.skrivUt())
    print(objekt2.skrivUt())
    print(objekt3.skrivUt())

    print("......................................................................")

    #Legger til 10 km i den siste sykkelen, så printer jeg ut den nye totalsummen
    objekt3.kjor(10)
    objekt3.hentKilometerstand()
    print("Legger til 10km:", objekt3.skrivUt())

hovedprogram()
