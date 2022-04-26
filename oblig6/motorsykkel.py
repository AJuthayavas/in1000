#Oppretter en klasse motorsykkel
class Motorsykkel:

    #Oppretter en konstruktør, med instansvariabler
    def __init__(self, merke, regstnr, kmavstand):
        self._merke = merke
        self._regstnr = regstnr
        self._kmavstand = kmavstand

    #Oppretter en metode
    def kjor(self, km):
        self._kmavstand += km

    #Oppretter en metode igjen
    def hentKilometerstand(self):
        return self._kmavstand

    #Oppretter en metode som returnerer info
    def skrivUt(self):
        #Denne funket visste ikke???
        #return "Merke: " + self._merke, "Registreringsnummer: " + self._regstnr, "Km: " + self._kmavstand
        #Men den under funka??? i don´t get it?
        return self._merke, self._regstnr, self._kmavstand
