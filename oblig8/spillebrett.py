from celle import Celle
from random import randint

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsNummer = 1 # Det første brettet som printes ut er generasjon 1, så første gang man trykker ENTER får vi gen. 2
        self._brett = [[Celle() for kolonne_celler in range(self._kolonner)] for rad_celler in range(self._rader)]

        self._generer()

    def tegnBrett(self):
        print('\n'*1)
        print("##############################")
        print("Printer ut det nye brettet ...")
        for rad in self._brett:
            for kolonne in rad:
                print(kolonne.hentStatusTegn(), end = "")
            print() # For å skape nye linje per rad

    def _generer(self):
        for rad in self._brett:
            for kolonne in rad:
                # 33.3% sjanse for at cellene blir født levende
                randomizer = randint(0,2)
                if randomizer == 1:
                    kolonne.settLevende()

    def oppdatering(self):
        # Cellene får hver sin liste, celler som holder seg levende / blir gjenopprettet, og celler som dør
        blir_resurrecta = []
        blir_myrdret = []

        for rad in range(len(self._brett)):
            for kolonne in range(len(self._brett[rad])):
                # Sjekk nabo per kvadrat
                sjekk_nabo = self.finnNabo(rad, kolonne)

                levende_nabo_teller = []

                for nabo_celle in sjekk_nabo:
                    # Sjekk i-live statusen for nabo cellene
                    if nabo_celle.erLevende():
                        levende_nabo_teller.append(nabo_celle)

                celle_objekt = self._brett[rad][kolonne]
                hoved_celle_status = celle_objekt.erLevende()

                # Hvis cellen er i live, sjekk naboens status
                if hoved_celle_status == True:
                    if len(levende_nabo_teller) < 2 or len(levende_nabo_teller) > 3:
                        blir_myrdret.append(celle_objekt)
                    if len(levende_nabo_teller) == 3 or len(levende_nabo_teller) == 2:
                        blir_resurrecta.append(celle_objekt)
                else:
                    if len(levende_nabo_teller) == 3:
                        blir_resurrecta.append(celle_objekt)

        # Gi cellene status
        for celle_item in blir_resurrecta:
            celle_item.settLevende()

        for celle_item in blir_myrdret:
            celle_item.settDoed()

        # Telle antall generasjoner
        self._generasjonsNummer += 1

    # Metoden for å printe ut generasjonsnummer
    def hentGenerasjonsnummer(self):
        print("# Generasjon:", self._generasjonsNummer)
        print("#################")



    def finnNabo(self, sjekk_rad, sjekk_kolonne):
        # Viser hvor dypt søket er
        let_etter_min = -1
        let_etter_max = 2

        # Tom liste blir opprettet for å appende inn naboer
        naboListe = []
        for rad in range(let_etter_min,let_etter_max):
            for kolonne in range(let_etter_min,let_etter_max):
                nabo_rad = sjekk_rad + rad
                nabo_kolonne = sjekk_kolonne + kolonne

                gyldig_nabo = True

                if (nabo_rad) == sjekk_rad and (nabo_kolonne) == sjekk_kolonne:
                    gyldig_nabo = False


                if (nabo_rad) < 0 or (nabo_rad) >= self._rader:
                    gyldig_nabo = False


                if (nabo_kolonne) < 0 or (nabo_kolonne) >= self._kolonner:
                    gyldig_nabo = False


                if gyldig_nabo:
                    naboListe.append(self._brett[nabo_rad][nabo_kolonne])
        return naboListe

    def finnAntallLevende(self):
        antallLevende = 0
        totalPlassbeholdere = 0

        for levende in range(0, self._rader):
            for levende2 in range(0, self._kolonner):
                if self._brett[levende][levende2].erLevende():
                    antallLevende += 1

        for doed in range(0, self._rader):
            for doed2 in range(0, self._kolonner):
                if self._brett[levende][levende2].hentStatusTegn():
                    totalPlassbeholdere += 1

        print("###################################################################")
        print("#", antallLevende, "//", totalPlassbeholdere, "     (Antall levende celler // Antall plasser totalt)")
        print("###################################################################")
