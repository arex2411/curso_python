import random
from random import randint
contador = 0

nombre = input("Nombre: ")
print(f"{nombre} he pensado un numero entre el 1 y el 100, tienes solo 8 intentos para adivinar cual crees que es el numero:")

aleatorio = randint(1,100)
print(aleatorio)
while contador<8:
    print(contador)
    contador = contador +1
    numero = int(input("Ingresa un numero:"))
    if numero <1 or numero >100:
        print("Este numero no esta permitido")
    elif numero < aleatorio:
        print("Su respuesta es incorrecta, has elegido un numero menor al secreto")
    elif numero > aleatorio:
        print(" Su respuesta es incorresta, has elegido un numero mayor al secreto")
    elif numero == aleatorio:
        print(f"Has ganado y te ha tomado {contador} intentos")
        break
else:
    print("Agotaste los 8 intentos")
