from Instruction import Instruction
from itertools import islice

def readFile():
    file = open("ejercicios/automata.txt", 'r')

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
            initial = line.split('\n')[0].split(',')[0]
            # print("Initial: "+str(initial))
        elif i >= 3:
            state = line.split('-')[0]
            options = line.split('\n')[0].split('>')[1].split('|')
            ins = Instruction(state, options)
            if state == initial:
                initial = ins
            automata.append(ins)

    file.close()

    return {'automata': automata, 'alphabet': alphabet, 'initial': initial, 'states': states}
