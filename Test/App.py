from Cidade import Cidade
from Mapa import Mapa

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
ponta1, ponta2 = mapa.identificar_pontas()
print(f"Pontas: {ponta1.nome}, {ponta2.nome}")

lista_espelhada = mapa.criar_lista_espelhada()
ligacoes = mapa.criar_ligacoes(lista_espelhada)

mapa.exibir_cidades()

for ligacao in ligacoes:
    print(f"Ligação: {ligacao.cidade1.nome} <--> {ligacao.cidade2.nome}")
