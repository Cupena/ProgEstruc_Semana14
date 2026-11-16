import random
import time

#Generar numeros aleatorios

def generar_intervalos(cantidad):
    elementos = [
        max(1, cantidad) // 4, max(1, cantidad // 2), cantidad 
    ]
    return sorted(set(elementos))

#Generar numeros

def generar_numero(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 1_000_000) for _ in range(cantidad) ]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

cantidad = int(input("Cuantos numeros: "))
intervalos = generar_intervalos(cantidad)
elementos, tiempo = generar_numero(cantidad)

print(intervalos)
print(elementos)
print(f"Duración: {tiempo/1000}")
