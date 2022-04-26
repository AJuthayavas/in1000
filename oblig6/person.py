#Oppretter en klasse person
class Person:

    #Oppretter en konstruktør, med instansvariabler
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    #Oppretter en metode
    def leggTilHobby(self):
        self._hobbyer = []
        streng = input("Legg til en hobby her: ")
        self._hobbyer.append(streng)

    #Oppretter en metode
    def skrivHobbyer(self):
        for i in self._hobbyer:
            return i

    #Oppretter en metode
    def skrivUt(self):
        print("Navn =", self._navn)
        print("Alder =", self._alder)
        print("................................")
        self._navn = input("Nytt navn: ")
        self._alder = input("Ny alder: ")
        print("................................")
        print("Ny bruker har blitt opprettet")

        #while loop opprettes for å kunne legge til hobbyer, eller avslutte koden
        statement = "zzz"
        while statement != "S":
            statement = input("Tast inn enten F/S. [F = opprett ny hobby] // [S = avslutt programmet]: ")


            if statement == "F":
                statement = input("[F = opprett ny hobby]: ")
                self._hobbyer.append(statement)


            elif statement == "S":
                print(".............................................................")
                print("Navn:", self._navn)
                print("Alder:", self._alder)
                print("Dine hobbyer:")
                for x in self._hobbyer:
                    print(x)

        quit()
