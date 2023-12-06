import os

from noticia import Noticia
from util import Util

def pegar_id():
    for n in noticias:
        print(n)
    id = int(input('ID da notícia: '))
    try:
        print('id da noticia',id)
        id = ids.index(id)
        print('index da noticia',id)
        return id
    except:
        print('Noticia invalida')
        return -1

def adicionar():
    titulo = input('Título da notícia: ')
    categoria = input('Categoria: ')
    texto = input('Texto: ')
    palavras_chave = []
    for i in range(3):
        palavras_chave.append(input(f'Palavra-chave {i+1}: '))
    if len(ids) == 0:
        id_atual = -1
    else:
        id_atual = ids[-1]
    nova_noticia = Noticia(id_atual+1,titulo,categoria,texto,palavras_chave)
    if nova_noticia.valida_noticia():
        print('Cadastrando noticia na base...')
        noticias.append(nova_noticia)
        ids.append(id_atual+1)
        Util.salvar_nova_noticia(nova_noticia)

def buscar():
    id = pegar_id()
    if id == -1:
        return
    print(noticias[id].mostrar_noticia())

def alterar():
    id = pegar_id()
    if id == -1:
        return
    noticia = noticias[id]
    while True:
        op = input('Qual campo deseja alterar?\n1. Titulo\n2. Categoria\n3. Texto\n4. Palavra-chave\n5. Finalizar\n6. Voltar')
        if op == '1':
            temp = input('Informe o novo título: ')
            noticia.titulo = temp
        elif op == '2':
            temp = input('Informe a nova categoria: ')
            noticia.categoria = temp
        elif op == '3':
            temp = input('Informe o novo texto: ')
            noticia.texto = temp
        elif op == '4':
            noticia.palavras_chave.clear()
            for i in range(3):
                noticia.palavras_chave.append(input(f'Palavra-chave {i+1}: '))
        elif op == '5':
            print('Atualizando noticia...')
            Util.atualizar_noticia(noticia,id)
            break
        elif op == '6':
            break
        else:
            print('opção inválida')

def deletar():
    id = pegar_id()
    if id == -1:
        return
    noticias.pop(id)
    ids.pop(id)
    print('Deletando noticia...')
    Util.deletar_noticia(id)

menu = '1. Adicionar notícia\n2. Buscar notícia\n3. Alterar notícia\n4. Deletar noticia\n5. Sair\n'

noticias,ids = Util.carregar_noticias()

while True:
    os.system('cls')
    print(menu)
    op = input('Opção: ')
    if op == '1':
        adicionar()
    elif op == '2':
        buscar()
    elif op == '3':
        alterar()
    elif op == '4':
        deletar()
    elif op == '5':
        break
    else:
        print('opção inválida')
    os.system('pause')
