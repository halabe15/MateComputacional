def run(automata, str):

    stand = [automata['initial'][0]]
    realStates = []
    fin = automata['final']
    autom = automata['automata']
    agrega = True
    tmp = []


    while agrega:
        agrega = False
        for state in stand:
            for ins in autom:
                res = ins.checkEpsilon(state)
                if res != None and res not in stand:
                    stand.append(res)
                    agrega = True
    for char in str:
        for state in stand:
            for ins in autom:
                res = ins.indicate(state, char)
                if res != None:
                    tmp.append(res)
        stand = tmp
        tmp = []
        agrega = True
        while agrega:
            agrega = False
            for state in stand:
                for ins in autom:
                    res = ins.checkEpsilon(state)
                    if res != None and res not in stand:
                        stand.append(res)
                        agrega = True




    for state in stand:
        if state not in tmp:
            tmp.append(state)

    stand = tmp

    print("Estados finales (donde se quedo despues de la solucion):")
    print(stand)

    tmp = False

    for state in fin:
        if state in stand:
            tmp = True

    if tmp:
        print("\nSi acepta")
    else:
        print("\nNo acepta")
