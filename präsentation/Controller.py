from data.Speicher import Speicher
from logik.Rechner import Rechner
from präsentation.View import View


class Controller:
    def __init__(self):
        self.speicher = Speicher()
        self.rechner = Rechner()
        self.view = View()

    def berechnen(self):
        a = self.view.hohleZahl("1. Zahl: ")
        b = self.view.hohleZahl("2. Zahl: ")
        operator = self.view.hohleOperator()

        ergebnis = self.rechner.rechne(a, b, operator)
        self.speicher.setLetztesEreignis(ergebnis)

        print("Ergebnis: ", self.speicher.getLetztesEreignis())
