from Dinosaurio import *


class triceraptors(Dinosaurio):
    def __init__(self, manada, tipo, atacante, patas, energia, posicion, probSobrevivir):
        super().__init__(manada, tipo, atacante, patas, energia, posicion, probSobrevivir)

    def mover(self, pos):
        if self.energia > 5:
            super().mover(pos)
            self.energia -= 5
        else:
            print("No hay energia")
    def sobrevivir(self):
        self.probSobrevivir = 8

    def __str__(self):
        return f"Triceraptors: {super().__str__()}"