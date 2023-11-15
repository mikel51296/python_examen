from Sipnosaurus import *
from Rex import *
from triceraptors import *
import random
def generarDino(cantidadTri):
        dinosaurios = []

        for _ in range(cantidadTri):
            dinosaurio = triceraptors(manada=True, tipo="Herbívoro", atacante=False, patas=4, energia=100, posicion=random.randint(0, 50), probSobrevivir=0)
            dinosaurios.append(dinosaurio)
            dinosaurio = Sipnosaurus(manada=False, tipo="Carnívoro", atacante=True, patas=2, energia=100, posicion=random.randint(0, 50), probSobrevivir=0)
            dinosaurios.append(dinosaurio)
            dinosaurio = Rex(manada=False, tipo="Carnívoro", atacante=True, patas=2, energia=100, posicion=random.randint(0, 50), probSobrevivir=0)
            dinosaurios.append(dinosaurio)

        return dinosaurios
