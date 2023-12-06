from noticia import Noticia
from os import system

class Util:
    def salvar_nova_noticia(noticia):
        """Salvar a noticia na base de dados"""
        try:
            with open('base_dados.csv','a') as f:
                f.write(noticia.all_data()+'\n')
                f.close()
                print('Notícia %s cadastrada com sucesso !!' % noticia.id)
        except Exception as e: #erro de entrada (falha ao abrir arquivo)
            print(e)

    def deletar_noticia(id):
        """Deletar noticia da base de dados"""
        try:
            with open('base_dados.csv', 'r') as f:
                arq = f.readlines()
                f.close()
            print(arq)
            print()
            arq.pop(id)
            print(arq)
            with open('base_dados.csv', 'w') as f:
                f.writelines(arq)
                f.close()
            print('Notícia %s deletada com sucesso !!' % id)
        except Exception as e: #erro de entrada (falha ao abrir arquivo)
            print(e)
    
    def atualizar_noticia(noticia, id):
        """Atualizar a noticia definida"""
        try:
            with open('base_dados.csv', 'r') as f:
                arq = f.readlines()
                f.close()
            arq[id] = noticia.all_data()
            with open('base_dados.csv', 'w') as f:
                f.writelines(arq)
                f.close()
            print('Notícia %s alterada com sucesso !!' % id)
        except Exception as e:
            print(e)

    def carregar_noticias():
        """Carrega a base de dados e a lista de indices"""
        noticias = []
        ids = []
        try:
            with open('base_dados.csv', 'r') as f:
                for linha in f.readlines():
                    noticia = linha.split(';')
                    noticias.append(Noticia(int(noticia[0]),noticia[1],noticia[2],noticia[3],noticia[4].split(',')))
                    ids.append(int(noticia[0]))
                f.close()
                print('Base carregada')
        except:
            try:
                print('Sem arquivo de banco de dados, criando arquivo...')
                open('base_dados.csv','a').close()
            except Exception as e:
                print(e)
        return noticias,ids