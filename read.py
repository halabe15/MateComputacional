def read():
    file = open("automata.txt", 'r')

    lines = file.readlines()

    for line in lines:
        initialState = line.split(',')[0]
        symbol = line.split(',')[1].split(':')[0]
        finalState = line.split(':')[1]

    file.close()
