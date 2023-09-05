import random as r
import os

mat = []

def gera_matriz():
    global mat
    mat = []
    n = int(input('Tamanho da matriz: '))
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(r.randint(0,100))
        mat.append(temp)
    print('Criando matriz %sx%s' % (n,n))

def mostra_matriz():
    n = len(mat)
    if n == 0:
        raise Exception('ERRO: Matriz deve ser inicializada')
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end="\t")
        print()  

def diag_principal():
    n = len(mat)
    if n == 0:
        raise Exception('ERRO: Matriz deve ser inicializada')
    for i in range(n):
        print('\t' * i, mat[i][i])

def diag_secundaria():
    n = len(mat)
    if n == 0:
        raise Exception('ERRO: Matriz deve ser inicializada')
    for i,j in zip(range(n),range(n-1,-1,-1)):
        print( '\t' * j, mat[i][j])

def menor():
    n = len(mat)
    if n == 0:
        raise Exception('Matriz deve ser inicializada')
    menor = mat[0][0]
    l = []
    c = []
    for i in range(n):
        for j in range(n):
            if(mat[i][j] < menor):
                menor = mat[i][j]
            
    for i in range(n):
        for j in range(n):
            if (menor == mat[i][j]):
                l.append(i)
                c.append(j)

    print('O menor valor encontrado foi: ', menor)
    if len(l) == 1:
        print(f'Ele está na linha {l[0]}, coluna {c[0]}')
    else:
        print('Ele aparece nas posições: ')
        for i,j in zip(l,c):
            print(f'Linha {i}, Coluna {j}')

menu = """1.Gerar matriz (Tamanho definido pelo usuário)
2.Mostrar matriz
3.Mostrar diagonal principal
4.Mostrar diagonal secundária
5.Mostrar menor valor e sua posição na matriz
6.Sair"""

opcoes = {'1': gera_matriz,
          '2': mostra_matriz,
          '3': diag_principal,
          '4': diag_secundaria,
          '5': menor,
          '6': exit,}



while True:
    os.system('cls')
    print(menu)
    op = input('Selecione a opcao: ')
    if(op not in opcoes.keys()):
        print('Opção Inválida')
        os.system('pause')
        continue
    try:
        opcoes[op]()
        os.system('pause')
    except Exception as err:
        print(err)
        os.system('pause')




