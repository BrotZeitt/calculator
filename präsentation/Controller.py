from data.Speicher import Speicher
from logik.Rechner import Rechner
#from präsentation.View import View
from präsentation.Gui import Gui

import tkinter as tk


class Controller:
    def __init__(self):
        self.__speicher = Speicher()
        self.__rechner = Rechner()

        root = tk.Tk()
        self.__gui = Gui(root, self)
        self.__gui.mainloop()

    def berechnen(self):
        a = self.__gui.hohleZahl(1)
        b = self.__gui.hohleZahl(2)
        operator = self.__gui.hohleOperator()

        ergebnis = self.__rechner.rechne(a, b, operator)
        self.__speicher.setLetztesEreignis(ergebnis)

        self.__gui.zeigeErgebnis(ergebnis)
