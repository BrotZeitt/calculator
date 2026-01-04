from data.Speicher import Speicher
from logik.Rechner import Rechner
from präsentation.View import View


class Controller:
    def __init__(self):
        self.__speicher = Speicher()
        self.__rechner = Rechner()
        self.__view = View()

    def berechnen(self):
        a = self.__view.hohleZahl("1. Zahl: ")
        b = self.__view.hohleZahl("2. Zahl: ")
        operator = self.__view.hohleOperator()

        ergebnis = self.__rechner.rechne(a, b, operator)
        self.__speicher.setLetztesEreignis(ergebnis)

        print("Ergebnis: ", self.__speicher.getLetztesEreignis())
