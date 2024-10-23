import math

class Cidade:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
        self.peso = 0

    def definir_distancia(self, outra_cidade):
        dist = math.sqrt((outra_cidade.x - self.x) ** 2 + (outra_cidade.y - self.y) ** 2)
        return dist

    def set_peso(self, peso):
        self.peso = peso