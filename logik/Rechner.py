

class Rechner:
    def __init__(self):
        pass

    def rechne(self, a: float, b: float, operator: str) -> float:
        
        match operator:
            case "+":
                ergebnis = self.__addition(a, b)
            case "-":
                ergebnis = self.__subtraction(a, b)
            case "*":
                ergebnis = self.__multiplikation(a, b)
            case "/":
                ergebnis = self.__divission(a, b)
            case _:
                ergebnis = False

        return ergebnis

    #Rechenoperationen    
    def __addition(self, a: float, b: float) -> float:
        return a + b
    
    def __subtraction(self, a: float, b: float) -> float:
        return a - b
    
    def __multiplikation(self, a: float, b: float) -> float:
        return a * b
    
    def __divission(self, a: float, b: float) -> float:
        return a / b