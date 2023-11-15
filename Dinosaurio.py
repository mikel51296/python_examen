import random


class Dinosaurio:
    def __init__(self, manada, tipo,atacante,patas,energia,posicion,probSobrevivir):
        self.manada = manada
        self.tipo = tipo
        self.atacante = atacante
        self.patas = patas
        self.energia = energia
        self.posicion = posicion
        self.probSobrevivir = probSobrevivir

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, value):
        self._posicion = value
    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, value):
        self._energia = value

    @property
    def probSobrevivir(self):
        return self._probSobrevivir

    @probSobrevivir.setter
    def probSobrevivir(self, value):
        self._probSobrevivir = value

    def comer(self):
        self.energia += 100

    def mover(self, pos):
        self.posicion = pos
    def sobrevivir(self):
        vivito = True
        if random.randint(0, 10) > self.probSobrevivir:
            vivito = False
        return vivito

    def __str__(self):
        return f"Manada: {self.manada}, Tipo: {self.tipo}, Atacante: {self.atacante}, Patas: {self.patas}, Energía: {self.energia}, Posición: {self.posicion}, Probabilidad de Sobrevivir: {self.probSobrevivir}"





