#Oppretter en klasse hund
class Hund:

    #Oppretter en konstruktør, med instansvariabler
    def __init__(self, alder, vekt, metthet):
        self._alder = alder
        self._vekt = vekt
        self._metthet = metthet

    #Oppretter en metode
    def hentInfo(self):
        return "Alder:", self._alder, "Vekt:", self._vekt

    #Oppretter en metode
    def spring(self):
        self._metthet -= 1
        print("--> Minsker metthet med 1, som blir", self._metthet)
        print("--> Og hvis mettheten er mindre enn 5, vil vekt minkes med 1")

        if 0 < self._metthet < 5:
            self._vekt -= 1

        return "Ny vekt =", self._vekt

    #Oppretter en metode med if statement
    def spis(self, heltall):
        self._heltall = heltall
        self._metthet += self._heltall
        print("--> Ny metthet blir:", self._metthet)
        print("--> Og hvis mettheten er større enn 7, vil vekt økes med 1")

        if self._metthet > 7:
            self._vekt += 1

        return "Ny vekt =", self._vekt
