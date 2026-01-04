

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

        eingabeFrame = ttk.Frame(self)
        eingabeFrame.pack()

        self.eingabebereich(eingabeFrame)

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


    def eingabebereich(self, parent):
        eingabefelder = [[["C", 1, "#fffff"], ["del", 2, "#fffff"], ["/", 1, "#fffff"]],
                         [[7, 1, "#fffff"], [8, 1, "#fffff"], [9, 1, "#fffff"], ["*", 1, "#fffff"]],
                         [[4, 1, "#fffff"], [5, 1, "#fffff"], [6, 1, "#fffff"], ["-", 1, "#fffff"]],
                         [[1, 1, "#fffff"], [2, 1, "#fffff"], [3, 1, "#ffff"], ["+", 1, "#fffff"]],
                         [[0, 2, "#fffff"], [",", 1, "#fffff"], ["=", 1, "#f21361"]]]
        
        for reihe in range(len(eingabefelder)):
            spalte = 0
            for feld in eingabefelder[reihe]:
                text = feld[0]
                breite = feld[1]
                farbe = feld[2]

                eingabeButton = ttk.Button(parent, text=text)
                eingabeButton.grid(row=reihe, column=spalte, columnspan=breite, sticky="nsew")

                spalte += breite