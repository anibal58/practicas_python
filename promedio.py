"""Promedio variable
Construir una función que se llame “promedio_variable”.
Esta función debe tomar un número arbitrario de
argumentos numéricos y devolver el promedio.
"""

def promedio(*args):
    total = 0
    terminos = 0
    n = 0
    
    for arg in args:
        print(arg)
        total += arg
        terminos += 1
    print(total / terminos)
    return total / terminos

print ("El promedio es: " + str(promedio(10,5,4,3)))

        