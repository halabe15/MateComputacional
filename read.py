from Instruction import Instruction
from itertools import islice

def read():
    file = open("automata.txt", 'r')

    instructions = []

    for i, line in enumerate(file):
        if i == 0:
            states = line.split('\n')[0].split(',')
            print("States: "+str(states))
        elif i == 1:
            alphabet = line.split('\n')[0].split(',')
            print("Alphabet: "+str(alphabet))
        elif i == 2:
            initial = line.split('\n')[0].split(',')
            print("Initial: "+str(initial))
        elif i == 3:
            final = line.split('\n')[0].split(',')
            print("Final: "+str(final))
        elif i >= 4:
            initialState = line.split(',')[0]
            symbol = line.split(',')[1].split(':')[0]
            finalState = line.split(':')[1].split('\n')[0]
            ins = Instruction(initialState, finalState, symbol)
            if initialState in states and finalState in states and symbol in alphabet:
                instructions.append(ins)
                # ins.show()
            else:
                print("Esta instruccion esta incorrecta, revisa que los estados existan o el simbolo este dentro del alfabeto.\n    Error en numero de linea: "+str(i+1))
                ins.show()

    print("Automata con # de trancisiones: "+str(len(instructions)))
    file.close()


    # with open('automata.txt') as f:
    #     for line in islice(f, 4, None):
    #         print (line)
