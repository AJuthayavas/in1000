#Oppretter en klasse dato
class Dato:

    #Oppretter en konstruktør, med instansvariabler
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._nyDag = int(nyDag)
        self._nyMaaned = int(nyMaaned)
        self._nyttAar = int(nyttAar)

    #Oppretter en metode
    def skrivUtDato(self):
        return self._nyDag, self._nyMaaned, self._nyttAar


    #Oppretter en metode
    def skrivUtAar(self):
        return self._nyttAar

    #Oppretter en metode med if or elif
    def sjekkDag(self):
        if self._nyDag == 15:
            print("Det er den 15. som betyr lønningsdag!")

        elif self._nyDag == 1:
            print("Det er den 1. som betyr ny måned, nye muligheter!")

        return self._nyDag

    #Oppretter en metode som returner verdier
    def streng(self):
        print("DD-MM-YYYY:", self._nyDag, "-", self._nyMaaned, "-", self._nyttAar)
