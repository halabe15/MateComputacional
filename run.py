def run(automata, str):

    stand = [automata['initial'][0]]
    realStates = []
    fin = automata['final']
    autom = automata['automata']
    agrega = True


    while agrega:
        agrega = False
        for state in stand:
            if state not in stand:
                stand.append(state)
            for ins in autom:
                res = ins.checkEpsilon(state)
                if res != None and res not in stand:
                    stand.append(res)
                    agrega = True
    print(stand)

    for state in stand:
        for char in str:
            for position in realStates:
                for ins in autom:
                    res = ins.indicate(position, char)
                    if res != None:
                        # print(res)
                        stand.append(res)
            # stand = tmp
    tmp = []

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
