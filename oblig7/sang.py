#Oppretter klasse sang
class Sang:

    #Konstruktøren opprettes her
    def __init__(self, _artist, _tittel):
        self._artist = _artist
        self._tittel = _tittel

    #Metode spill printer ut sanger på en ryddig måte
    def spill(self):
        spiller = "Spiller: " + self._tittel + " av " + self._artist
        print(spiller)

    #Metode som sjekker artist
    def sjekkArtist(self, navn):
        nyArtist = navn.lower()
        self._artist = self._artist.lower()

        for ord in nyArtist.split():
            if ord in self._artist.split():
                return True
        return False

   #Metode som sjekker tittel
    def sjekkTittel(self, tittel):
         if tittel.lower() == self._tittel.lower():
             return True
         else:
             return False

     #Metode som sjekker både artist og tittel
    def sjekkArtistOgTittel(self, artist, tittel):
         if artist.lower() in self._artist.lower() and tittel.lower() in self._tittel.lower():
             return True
         else:
             return False
