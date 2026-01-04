

import tkinter as tk
from tkinter import ttk



class Gui(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.pack()

        self.__ergebnis = ttk.Label(self, text="XXXXX")
        self.__ergebnis.pack()

        self.__ersteZahlEingabe = ttk.Entry(self)
        self.__ersteZahlEingabe.pack()

        self.__zweiteZahlEingabe = ttk.Entry(self)
        self.__zweiteZahlEingabe.pack()

        self.__operatorEingabe = ttk.Entry(self)
        self.__operatorEingabe.pack()

        self.__berechnenButton = ttk.Button(self, text="Berechnen", command=controller.berechnen)
        self.__berechnenButton.pack()

    def hohleZahl(self, zahl) -> float:
        match zahl:
            case 1:
                return int(self.__ersteZahlEingabe.get())
            case 2:
                return int(self.__zweiteZahlEingabe.get())
            case _:
                return None 
            
    def hohleOperator(self) -> str:
        return self.__operatorEingabe.get()
    
    def zeigeErgebnis(self, ergebnis):
        print(ergebnis)
        self.__ergebnis.config(text=str(ergebnis))


