class Instruction:
    initialState = ""
    finalState = ""
    symbol = ""

    def __init__(self, initial, final, symbol):
        self.initialState = initial
        self.finalState = final
        self.symbol = symbol

    def __str__(self):
        return self.initialState+", "+self.symbol+": "+self.finalState

    def show(self):
        print("\n-----------------")
        print("Estado inicial: "+self.initialState)
        print("Estado final: "+str(self.finalState))
        print("Simbolo: "+str(self.symbol))
        print("-----------------\n")

    def indicate(self, state, symbol):
        if state == self.initialState and symbol == self.symbol:
            return self.finalState
        return None

    def checkEpsilon(self, state):
        if self.symbol == 'E' and state == self.initialState:
            return self.finalState
        return None
