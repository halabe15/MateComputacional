# Proyecto Matematicas Computacionales
#
#       Isaac Halabe
#       Matricula: A01021800
#       Contacto: A01021800@itesm.mx
#
#       Victor Ferzuli
#       Matricula: A01022166
#       Contacto: A01022166@itesm.mx

# Importacion de archivos
from read import readFile
from user import readUser
from run import run

automata = readFile()
cadena = readUser()
run(automata, cadena)
