
from util import Util
from grafo import Grafo

grafo = Grafo()
util = Util()

def montar_tabela_heuristica(lista_heuristica):
    grafo.criar_lista_heuristica(util.pegar_arquivo(tipo='heuristica'), lista_heuristica)
    print("Quantidade de cidades/estados: %s " % len(lista_heuristica))
    for i in lista_heuristica:
        print(i)
    
def montar_matriz_adjacencia(matrizAdjacencia, lista_heuristica):
    grafo.preencher_matriz_adjacencia(util.pegar_arquivo(tipo='mapa'), matrizAdjacencia, lista_heuristica)
    print("Matriz de adjacencia")
    grafo.mostrar_matriz_adjacencia(matrizAdjacencia, lista_heuristica)

lista_heuristica = []
montar_tabela_heuristica(lista_heuristica)
matriz_adjacencia = []
montar_matriz_adjacencia(matriz_adjacencia, lista_heuristica)