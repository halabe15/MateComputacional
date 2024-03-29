from Instruction import Instruction
from itertools import islice

def readFile():
    file = open("ejercicios/automata4.txt", 'r')

    automata = []

    for i, line in enumerate(file):
        if i == 0:
            states = line.split('\n')[0].split(',')
            # print("States: "+str(states))
        elif i == 1:
            alphabet = line.split('\n')[0].split(',')
            # alphabet.append('E')
            # print("Alphabet: "+str(alphabet))
        elif i == 2:
            initial = line.split('\n')[0].split(',')
            # print("Initial: "+str(initial))
        elif i == 3:
            final = line.split('\n')[0].split(',')
            # print("Final: "+str(final))
        elif i >= 4:
            initialState = line.split(',')[0]
            symbol = line.split(',')[1].split(':')[0]
            finalState = line.split(':')[1].split('\n')[0]
            ins = Instruction(initialState, finalState, symbol)
            if initialState in states and finalState in states and symbol in alphabet or symbol == 'E':
                automata.append(ins)
                # ins.show()
            else:
                if symbol != 'E':
                    print("Esta instruccion esta incorrecta, revisa que los estados existan o el simbolo este dentro del alfabeto.\n    Error en numero de linea: "+str(i+1))
                    ins.show()

    # print("Automata con # de trancisiones: "+str(len(automata)))

    file.close()

    return {'automata': automata, 'alphabet': alphabet, 'initial': initial, 'final': final}
