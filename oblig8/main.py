from spillebrett import Spillebrett


def main():
    # Bruker taster inn info
    input_rad = int(input("Tast inn ønsket antall rader: "))
    input_kolonne = int(input("Tast inn ønsket antall kolonner: "))

    # Opprett nytt brett
    gameOfLifeBrett = Spillebrett(input_rad, input_kolonne)

    gameOfLifeBrett.tegnBrett()

    brukerHandlinger = ""

    while brukerHandlinger != "Q":
        brukerHandlinger = input("Press ‘ENTER’ for å legge til en ny generasjon eller ‘Q’ for å avslutte! ")

        if brukerHandlinger == "":
            gameOfLifeBrett.oppdatering()
            gameOfLifeBrett.tegnBrett()
            gameOfLifeBrett.finnAntallLevende()
            gameOfLifeBrett.hentGenerasjonsnummer()


main()
