class Celle:
   # Konstruktør
    def __init__(self):
        self._status = "død"

    # Endre status
    def settLevende(self):
        self._status = "levende"

    def settDoed(self):
        self._status = "død"

    # Hente status
    def erLevende(self):
        if self._status == "levende":
            return True
        return False

    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        return "."
