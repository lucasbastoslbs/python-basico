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
#dimensao = 3
#tab = [[0 for _ in range(dimensao)]] * dimensao
tab = [[0,0,0],[0,0,0],[0,0,0]]
#print(tab)
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

l = 1
c = 0
for i in range(1,10):
    l, c = proximo(l,c,i,tab)
    exibir()