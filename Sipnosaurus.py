import random
from Dinosaurio import *
from triceraptors import *

class Sipnosaurus(Dinosaurio):
    def __init__(self, manada, tipo, atacante, patas, energia, posicion, probSobrevivir):
        super().__init__(manada, tipo, atacante, patas, energia, posicion, probSobrevivir)

    def mover(self, pos):
        if self.energia > 2:
            super().mover(pos)
            self.energia -= 2
        else:
            print("No hay energia")

    def sobrevivir(self):
        self.probSobrevivir = 5

    def atacar(self, presa):
        if self.energia > 20:
            self.energia -= 20
            if isinstance(presa, triceraptors):
                vivito = True
                num = random.randint(0, 10)
                if num < 2:
                    vivito = False
                return vivito
            else:
                vivito = True
                num = random.randint(0, 10)
                if num < 5:
                    vivito = False
                return vivito
        else:
            print("No hay energia")
    def __str__(self):
        return f"Sipnosaurus: {super().__str__()}"
