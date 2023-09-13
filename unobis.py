""""
Ejercicio 1 adicional: Mostrar y eliminar
Utilizando un bucle “while”, elaborar un código
que imprima en pantalla cada uno de los
elementos de una lista y simultáneamente los
elimine, hasta quedar vacía.
"""

lista = [2,3,6,8,43,23,2,1]
##contador = len(lista)
i = 0

while i < len(lista):
    print(lista[i])
    lista.pop(0)

