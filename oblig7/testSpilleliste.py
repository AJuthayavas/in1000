from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():

    allMusikk = Spilleliste("Hele musikkbiblioteket")
    print("\n")
    print("Nå printes hele musikkbiblioteket:")
    print("...............................")
    C = allMusikk.lesFraFil("musikk.txt")
    for sang in C:
        print(sang._artist + " : " + sang._tittel)


    print("\n")


    print("Tester spillAlle, så nå skal alle sangene spilles:")
    print("...............................")
    spiller = allMusikk.spillAlle()
    for sang in spiller:
        print(sang)


    print("\n")


    print("Nå printes hele musikkbiblioteket igjen, men med den nye sangen:")
    nySang = Sang("Mil etter mil", "Jahn")
    print(".............................")
    X = allMusikk.leggTilSang(nySang)
    for sang in X:
        print(sang._artist + " : " + sang._tittel)


    print("\n")


    nySang = Sang("Mil etter mil", "Jahn")
    print("Spiller ny sang:")
    X = allMusikk.spillSang(nySang)
    print(X)


    print("\n")


    print("Tester spillAlle, så nå skal alle sangene spilles, inkl. den nye:")
    print("...............................")
    spiller = allMusikk.spillAlle()
    for sang in spiller:
        print(sang)


    print("\n")


    funnetSang = allMusikk.finnSang("Mil etter mil")
    if funnetSang is not None:
        print("Fant sangen:")
        print(allMusikk.spillSang(funnetSang))
    else:
        print("Fant ikke sangen med tittel:\n")
        assert(funnetSang in allMusikk.hentArtistUtvalg("Jahn"))
        print()



    print("\n")


    #Tester om flere sanger returneres for samme artist
    queenListe = allMusikk.hentArtistUtvalg("Queen")
    print("Spiller sanger med Queen hentet fra listen:")
    for queenSang in queenListe:
        print(queenSang.spill())


    print("\n")


    allMusikk.fjernSang(funnetSang)
    assert(not (funnetSang in allMusikk.hentArtistUtvalg("Jahn")))

    print("Nå skal funnetSang fjernes, deretter printer jeg ut listen på nytt:")
    print("Sangen som som skal fjernes er Mil etter mil av Jahn:")
    print("...............................")
    spiller = allMusikk.spillAlle()
    for sang in spiller:
        print(sang)


hovedprogram()
