import random as r

def gerador(c):
    if(type(c) == int):
        return str(r.randint(0,9))
    elif(type(c) == str):
        return letras[r.randint(0,25)]

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
modelo = ('A','A','A',1,'A',1,1)
placa = ''

for c in modelo:
    placa += gerador(c)

print(placa)