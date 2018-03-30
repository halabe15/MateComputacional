def run(automata, str):

    stand = [automata['initial'][0]]
    tmp = []
    fin = automata['final']
    autom = automata['automata']

    for char in str: #1101
        print(char)
        print (stand)
        for state in stand:
            for ins in autom:
                res = ins.indicate(state, char)
                if res != None:
                    print(res)
                    tmp.append(res)
        stand = tmp
        tmp = []

    for state in stand:
        if state not in tmp:
            tmp.append(state)

    stand = tmp

    print("Estados finales (donde se quedo despues de la solucion):")
    print(stand)

    for state in fin:
        if state in stand:
            print("Si acepta")
        else:
            print("No acepta")
