from sang import Sang

#Oppretter klasse spilleliste
class Spilleliste:

    #Konstruktør
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    #Metode som leser fra txt-fil
    def lesFraFil(self, filnavn):
        musikkfil = open(filnavn, "r")

        #Splitter linjene fra filen, og legger dem i liste
        for line in musikkfil:
            alleData = line.strip().split(";")
            sang = Sang(alleData[1], alleData[0])
            self._sanger.append(sang)

        musikkfil.close()

    #Legg til sang
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    #Fjern sanger fra lista
    def fjernSang(self, slettSang):
        self._sanger.remove(slettSang)


    #Spill av en bestemt sang
    def spillSang(self, spillSang):
        spillSang.spill()

    #Spill av alle sanger fra lista
    def spillAlle(self):
        spiller = []
        for sang in self._sanger:
            spiller.append(sang.spill())

    #Finn sang
    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang._tittel == tittel:
                return sang
        return None

    def hentArtistUtvalg(self, artistnavn):
        sangliste = []

        for sanger in self._sanger:
            if sanger.sjekkArtist(artistnavn):
                sangliste.append(sanger)

        return sangliste
