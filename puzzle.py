import random as r
import os
import msvcrt

def exibir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j],end="\t")
        print("")

def cima(l,c):
    if(l == 0):
        return
    matriz[l][c] = matriz[l-1][c]
    matriz[l-1][c] = 0
    return l-1,c

def baixo(l,c):
    if l == len(matriz):
        return
    matriz[l][c] = matriz[l+1][c]
    matriz[l+1][c] = 0
    return l+1,c

def esquerda(l,c):
    if(c == 0):
        return
    matriz[l][c] = matriz[l][c-1]
    matriz[l][c-1] = 0
    return l,c-1

def direita(l,c):
    if(c == len(matriz)):
        return
    matriz[l][c] = matriz[l][c+1]
    matriz[l][c+1] = 0
    return l,c+1

def iniciaMatriz(n):
    numeros = [ele for ele in range(n*n)]
    lista = []
    lista = [[1,0,2],[3,4,5],[6,7,8]]
    return lista,0,1
    for i in range(n):
        temp = []
        for j in range(n):
            z = numeros.pop(r.randint(0,len(numeros)-1))
            if z == 0:
                l = i
                c = j
            temp.append(z)
        lista.append(temp)
    return lista,l,c

def estagio_final(n):
    fim = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(i * n + j)
        fim.append(temp)
    if(fim == matriz):
        return True
    return False    

n = int(input('Tamanho da matriz: '))
matriz,linha,coluna = iniciaMatriz(n)

menu = {'w': cima,
        's':baixo,
        'a':esquerda,
        'd':direita,
        't':exit}

while True:
    os.system('cls')
    exibir(matriz)
    #op = input('')
    try:
        op = msvcrt.getch().decode()
        if op == 't':
            break
        linha, coluna = menu[op](linha,coluna)
        if estagio_final(n):
            os.system('cls')
            exibir(matriz)
            print('\nfim')
            break
    except:
        pass
    
    
