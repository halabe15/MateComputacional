class Instruction:
    initialState = ""
    finalState = ""
    symbol = ""

    def __init__(self, initial, final, symbol):
        self.initialState = initial
        self.finalState = final
        self.symbol = symbol

    def show(self):
        print("\n-----------------")
        print("Estado inicial: "+self.initialState)
        print("Estado final: "+str(self.finalState))
        print("Simbolo: "+str(self.symbol))
        print("-----------------\n")
