class Instruction:
    state = ""
    options = []

    def __init__(self, state, options):
        self.state = state
        self.options = options

    def __str__(self):
        return self.state+"->"+('|'.join(self.options))

    def show(self):
        print("\n-----------------")
        print("Estado: "+self.state)
        print("Opciones: "+str(self.options))
        print("-----------------\n")

    # def indicate(self, state, symbol):
    #     if state == self.initialState and symbol == self.symbol:
    #         return self.finalState
    #     return None
    #
    # def checkEpsilon(self, state):
    #     if self.symbol == 'E' and state == self.initialState:
    #         return self.finalState
    #     return None
