import Dinosaurio


class triceraptors(Dinosaurio.Dinosaurio):
    def __init__(self, manada, tipo,atacante,patas,energia,posicion,):
        super(Dinosaurio, self).__init__(manada, tipo,atacante,patas,energia,posicion)
    def mover(self, pos):
        super().mover()
        self.energia -= 5