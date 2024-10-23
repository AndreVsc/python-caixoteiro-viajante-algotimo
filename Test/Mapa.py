from Ligacao import Ligacao 


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

    def exibir_cidades(self):
        for cidade in self.cidades:
            print(f"{cidade.nome}: ({cidade.x}, {cidade.y}) - Peso: {cidade.peso:.2f}")