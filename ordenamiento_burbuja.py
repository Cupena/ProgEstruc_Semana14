import random

#Generar numeros aleatorios

def generar_intervalos(cantidad):
    elementos = [
        max(1, cantidad) // 4, max(1, cantidad // 2), cantidad 
    ]
    return sorted(set(elementos))

cantidad = int(input("Cuantos numeros: "))
elementos = generar_intervalos(cantidad)

print(elementos)
