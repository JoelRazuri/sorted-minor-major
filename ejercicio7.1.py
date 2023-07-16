"""
    Escribir una función que reciba una tupla de elementos e indique si se encuentran 
    ordenados de menor a mayor o no.
"""


def es_ordenada(tupla):
    # Recibe una tupla y devuelve True si los elementos estan ordenados de menor a mayor, o False sino

    i = 0
    longitud = len(tupla) - 1
    condicion = True

    while i<longitud and condicion:
        if tupla[i]>tupla[i+1]:
            condicion = False
            break
        i+=1
    
    if condicion:
        print("La tupla esta ordenada")
    else:
        print("La tupla esta desordenada")
    

es_ordenada((1,4,2,3,6))
es_ordenada((1,1,3,5,7,10))
es_ordenada((1,1,3))