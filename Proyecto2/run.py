from Stack import Stack
import copy

def run(automata, str):

    stackStates = Stack()
    stackAlphabet = Stack()
    stackStates.push(automata['initial'])
    autom = automata['automata']
    states = automata['states']
    alphabet = automata['alphabet']
    agrega = True


    # Revisar si antes de empezar tenemos Epsilons cerca
    # while agrega:
    #     agrega = False
        # Para cada linea del automata
    for ins in stackStates.items:
        for option in ins.options:
            for char in option:
                if char in states:
                    
                elif char in alphabet:
                    print("alfabeto")

                else:
                    return print("Ocurrio un error, valor no encontrado: ")+ins


    # # Para cada caracter de la cadena
    # for char in str:
    #     # Para cada estado en el que estamos posicionados
    #     for state in stand:
    #         # Para cada linea del automata
    #         for ins in autom:
    #             # Revisa si hay una linea que te envia desde la posicion actual con el simbolo, de ser asi regresa el valor a donde te envia
    #             res = ins.indicate(state.peek(), char)
    #             if res != None:
    #                 # Hacemos una copia del segundo camino para agregarlo
    #                 cop = copy.deepcopy(state)
    #                 cop.push(res)
    #                 tmp.append(cop)
    #     stand = tmp
    #     tmp = []
    #     agrega = True
    #     while agrega:
    #         agrega = False
    #         # Para cada estado en el que estamos posicionados
    #         for state in stand:
    #             # Para cada linea del automata
    #             for ins in autom:
    #                 # Revisa si hay un epsilon enviando la posicion actual, de ser asi regresa el valor a donde te envia
    #                 res = ins.checkEpsilon(state.peek())
    #                 if res != None:
    #                     # Para no meter valores repetidos -------
    #                     jump = False
    #                     for st in stand:
    #                         if st.peek() == res:
    #                             jump = True
    #                     if not jump:
    #                         # Hacemos una copia del segundo camino para agregarlo
    #                         cop = copy.deepcopy(state)
    #                         cop.push(res)
    #                         stand.append(cop)
    #                         agrega = True
    #                     # Para no meter valores repetidos -------
    #
    #
    # # Limpiamos repetidos -----------
    # for state in stand:
    #     if state not in tmp:
    #         tmp.append(state)
    # stand = tmp
    # # Limpiamos repetidos -----------
    #
    #
    # # print("Estados finales (donde se quedo despues de la solucion):")
    # # for stack in stand:
    # #     print(stack.peek(), end=' ')
    #
    # tmp = False
    # print()
    #
    # for state in stand:
    #     if state.peek() in fin:
    #         print("\nSi acepta")
    #         print(state)
    #         tmp = True
    #
    # if not tmp:
    #     print("\nNo acepta")
