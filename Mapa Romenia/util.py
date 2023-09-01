from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from grafo import Grafo
import os

class Util:
   
    def pegar_arquivo(self, tipo):
        filetypes = (
            ('Arquivos de mapa', '*.map'),
            ('All Files', '*'),
        )
        try:
            file = fd.askopenfilenames(title=f'Selecione o arquivo de {tipo}',filetypes=filetypes,initialdir=os.path.curdir)
            if not file:
                raise Exception('Favor carregar o arquivo')
        except:
            showinfo(title='Erro!', message='arquivo de heuristica não carregado')
        return file[0]
    
    def montar_tabela_heuristica(self, listaHeuristica):
        grafo = Grafo()
        grafo.criar_lista_heuristica(self.pegar_arquivo('heuristica'), listaHeuristica)
    
    def montar_matriz_adjacencia(self, matrizAdjacencia, listaHeuristica):
        grafo = Grafo()
        grafo.preencher_matriz_adjacencia(self.pegar_arquivo('mapa'), matrizAdjacencia, listaHeuristica)
        print("Matriz de adjacencia")
        grafo.mostrar_matriz_adjacencia(matrizAdjacencia, listaHeuristica)