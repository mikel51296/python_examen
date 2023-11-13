class Dinosaurio:
    def __init__(self, manada, tipo,atacante,patas,energia,posicion):
        self.manada = manada
        self.tipo = tipo
        self.atacante = atacante
        self.patas = patas
        self.energia = energia
        self.posicion = posicion

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def radio(self, energia):
        self._energia = energia

    def comer(self):
        self.energia =+ 100

    def mover(self,pos):
        self.posicion = pos