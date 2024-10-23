import math
import matplotlib.pyplot as plt

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

class Ligacao:
    def __init__(self, cidade1, cidade2):
        self.cidade1 = cidade1
        self.cidade2 = cidade2

class Mapa:
    def __init__(self):
        self.cidades = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def organizar_cidades(self):
        self.cidades.sort(key=lambda cidade: cidade.x + cidade.y)

    def definir_pesos(self):
        for cidade in self.cidades:
            peso = 0
            for outra_cidade in self.cidades:
                if cidade != outra_cidade:
                    peso += cidade.definir_distancia(outra_cidade)
            cidade.set_peso(peso)

    def identificar_pontas(self):
        self.cidades.sort(key=lambda cidade: cidade.peso, reverse=True)
        ponta1, ponta2 = self.cidades[0], self.cidades[1]
        return ponta1, ponta2

    def criar_lista_espelhada(self):
        self.cidades.sort(key=lambda cidade: cidade.peso)
        n = len(self.cidades)
        lista_espelhada = [None] * n
        centro = n // 2
        for i in range(centro):
            lista_espelhada[centro - i - 1] = self.cidades[i]
            lista_espelhada[centro + i] = self.cidades[n - i - 1]
        if n % 2 != 0:
            lista_espelhada[centro] = self.cidades[centro]
        return lista_espelhada

    def criar_ligacoes(self, lista_espelhada):
        ligacoes = []
        for i in range(len(lista_espelhada) - 1):
            ligacoes.append(Ligacao(lista_espelhada[i], lista_espelhada[i + 1]))
        return ligacoes

    def desenhar_mapa(self, lista_espelhada, ligacoes):
        fig, ax = plt.subplots()

        for cidade in lista_espelhada:
            ax.plot(cidade.x, cidade.y, 'bo')
            ax.text(cidade.x + 0.1, cidade.y + 0.1, cidade.nome, fontsize=9)

        for ligacao in ligacoes:
            x_values = [ligacao.cidade1.x, ligacao.cidade2.x]
            y_values = [ligacao.cidade1.y, ligacao.cidade2.y]
            ax.plot(x_values, y_values, 'k-')  # é a linha preta

        ax.set_xlim(min(cidade.x for cidade in lista_espelhada) - 1, 
                     max(cidade.x for cidade in lista_espelhada) + 1)
        ax.set_ylim(min(cidade.y for cidade in lista_espelhada) - 1, 
                     max(cidade.y for cidade in lista_espelhada) + 1)

        ax.set_xlabel('Coordenada X')
        ax.set_ylabel('Coordenada Y')
        ax.set_title('Representação 2D do Mapa de Cidades')
        plt.grid(True)
        plt.show()

cidade1 = Cidade("Cidade A", 1, 2)
cidade2 = Cidade("Cidade B", 3, 1)
cidade3 = Cidade("Cidade C", 0, 4)
cidade4 = Cidade("Cidade D", 2, 5)

mapa = Mapa()
mapa.adicionar_cidade(cidade1)
mapa.adicionar_cidade(cidade2)
mapa.adicionar_cidade(cidade3)
mapa.adicionar_cidade(cidade4)

mapa.definir_pesos()
lista_espelhada = mapa.criar_lista_espelhada()
ligacoes = mapa.criar_ligacoes(lista_espelhada)

mapa.desenhar_mapa(lista_espelhada, ligacoes)
