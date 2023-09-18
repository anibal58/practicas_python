"""
    Mostrar y eliminar
    Utilizando un bucle “while”, elaborar un código
    que imprima en pantalla cada uno de los
    elementos de una lista y simultáneamente los
    elimine, hasta quedar vacía.
"""


lista = [1,6,435,76,675,34,34,45,96]

while len(lista) > 0:
    print(lista[0])
    lista.pop(0)

print(lista)