import random

import FactoriaDino
from Dinosaurio import Dinosaurio
from triceraptors import triceraptors

lista = FactoriaDino.generarDino(3)
cont = 0
respuesta = 's'
while respuesta == 's' and len(lista) > 2:
    opcion = random.randint(1,3)
    if opcion == 1:
        lista[cont].mover(random.randint(0, 50))
        print(f"\nSe ha modificado: {lista[cont]}" )
        print(f"Su energia es de: {lista[cont].energia}")
        print(f"su posicion es de: {lista[cont].posicion}")
    if opcion == 2:
        lista[cont].comer()
        print(f"\nSe ha modificado: {lista[cont]}")
        print(f"Su energia es de: {lista[cont].energia}")
    if opcion == 3:
        if isinstance(lista[cont], triceraptors):
            print("No puede atacar")
        else:
            if len(lista) > 2:
                numLen = len(lista) - 1
                numDino = random.randint(0, numLen)
                while numDino == cont:
                    numDino = random.randint(0, numLen)
                print(f"\nEl depredador es: {lista[cont]}")
                print(f"La presa es: {lista[numDino]}")
                print(cont)
                print(numDino)
                entra = False
                if not lista[cont].atacar(lista[numDino]):
                    print(f"Se ha eliminado el atacante: {lista[cont]}")
                    lista.remove(lista[cont])
                    entra = True
                if cont < numDino and entra:
                    if not lista[numDino-1].sobrevivir():
                        print(f"\nSe ha eliminado la presa: {lista[numDino - 1]}")
                        lista.remove(lista[numDino - 1])
                else:
                    if not lista[numDino].sobrevivir():
                        print(f"\nSe ha eliminado la presa: {lista[numDino]}")
                        lista.remove(lista[numDino])
            else:
                print("No hay 2 dinosaurios")
    cont += 1
    if cont >= len(lista)-1:
        cont = 0
    respuesta = input('\nQuieres seguir (s/n)?: ')
