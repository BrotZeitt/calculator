

class Speicher:
    def __init__(self):
        #Ergebnis des letzten Ereignisses
        self.__letztesEreignis = None

    def setLetztesEreignis(self, neu):
        self.__letztesEreignis = neu

    def getLetztesEreignis(self) -> str:
        return self.__letztesEreignis