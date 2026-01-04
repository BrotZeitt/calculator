


class View:
    def __init__(self):
        pass

    def zeigeErgebnis(self, ergebnis):
        print("= ", ergebnis)
        
    def hohleZahl(self, text) -> float:
        return float(input(text))

    def hohleOperator(self) -> float:
        return str(input("Operator (+; -; *; /): "))