from Stack import Stack
import copy

def run(automata, str):

    initial = Stack()
    initial.push(automata['initial'][0])
    stand = [initial]
    realStates = []
    fin = automata['final']
    autom = automata['automata']
    agrega = True
    tmp = []

    while agrega:
        agrega = False
        for state in stand:
            for ins in autom:
                res = ins.checkEpsilon(state.peek())
                if res != None: #and res not in stand:
                    jump = False
                    for st in stand:
                        if st.peek() == res:
                            jump = True
                    if not jump:
                        cop = copy.deepcopy(state)
                        cop.push(res)
                        stand.append(cop)
                        agrega = True
    for char in str:
        for state in stand:
            for ins in autom:
                res = ins.indicate(state.peek(), char)
                if res != None:
                    cop = copy.deepcopy(state)
                    cop.push(res)
                    tmp.append(cop)
        stand = tmp
        tmp = []
        agrega = True
        while agrega:
            agrega = False
            for state in stand:
                for ins in autom:
                    res = ins.checkEpsilon(state.peek())
                    if res != None: #and res not in stand:
                        jump = False
                        for st in stand:
                            if st.peek() == res:
                                jump = True
                        if not jump:
                            co = copy.deepcopy(state)
                            co.push(res)
                            stand.append(co)
                            agrega = True



    for state in stand:
        if state not in tmp:
            tmp.append(state)

    stand = tmp

    print("Estados finales (donde se quedo despues de la solucion):")
    for stack in stand:
        print(stack.peek(), end=' ')

    tmp = False
    print()

    for state in stand:
        if state.peek() in fin:
            print(state)
            tmp = True

    if tmp:
        print("\nSi acepta")
    else:
        print("\nNo acepta")
