"""
0 0 0
0 0 0
0 1 0

4 9 2
3 5 7
8 1 6

0 0 2
3 0 0
0 1 0
"""

def mat_dinamica(n):
    if(n%2 == 0):
        raise Exception('Somente numero ímpar')
    mat = []
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append(0)
        mat.append(temp)
    return mat

def exibir():
    for i in tab:
        print(i)
    print()

def proximo(l,c,num,tab):
    pl = l+1
    pc = c+1
    if pl == len(tab):
        pl = 0
    if pc == len(tab):
        pc = 0
    if tab[pl][pc] != 0:
        pl = l-1
        pc = c
        tab[pl][pc] = num
    else:
        tab[pl][pc] = num
    return pl,pc

dimensao = 9
tab = mat_dinamica(dimensao)
#tab = [[0,0,0],[0,0,0],[0,0,0]]
#print(tab)
l = dimensao-2
c = int(dimensao/2)-1
for i in range(1,dimensao*dimensao+1):
    l, c = proximo(l,c,i,tab)
    exibir()