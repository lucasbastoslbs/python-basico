from cidade import Cidade

class Grafo:
    def criar_lista_heuristica(self, arquivo, lista):
        with open(arquivo) as f:
            for line in f.readlines():
                resposta = line
                resposta = resposta.split('@')
                lista.append(Cidade(resposta[0], int(resposta[1])))
        f.close()
    
    def pega_indice(self, nome_cidade, lista_heuristica):
        idx = 0
        for i in lista_heuristica:
            if (i.nome == nome_cidade):
                return idx
            idx += 1
        return -1

    def preencher_matriz_adjacencia(self, arquivo, matriz, lista_heuristica):
        #inicializar a matriz de adjacencia
        for i in range(len(lista_heuristica)):
            temp = []
            for j in range(len(lista_heuristica)):
                temp.append(0)
            matriz.append(temp)
        with open(arquivo) as f:
            for line in f.readlines():
                resposta = line.split("@")
                origem = self.pega_indice(resposta[0], lista_heuristica)
                destino = self.pega_indice(resposta[1], lista_heuristica)
                try:
                    matriz[origem][destino] = int(resposta[2])
                except:
                    print("Problemas de índices na matriz de adjacência!")
        f.close()

    def mostrar_matriz_adjacencia(self, matriz, lista_heuristica):
        for i in lista_heuristica:
            print("\t" + i.nome[0],end='')
        print()
        
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if (j == 0):
                    print(lista_heuristica[i].nome[0] + "\t",end='')
                print('%s\t' % matriz[i][j],end='')
            print()
    
    def mostrar_lista_heuristica(self, lista_heuristica):
        for i in lista_heuristica:
            print(i)