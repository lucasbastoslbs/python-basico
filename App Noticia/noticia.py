class Noticia:
    def __init__(self,id,titulo,categoria,texto,palavras_chave):
        """Construtor classe noticia
        Args:
        titulo - título da notícia
        categoria - tipo de notícia (entretenimento,esporte,política)
        texto - texto da notícia
        palavra_chave - 3 palavras-chave da notícia
        """
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.texto = texto
        self.palavras_chave = palavras_chave

    def separa_chaves(self):
        return self.palavras_chave[0] + ',' + self.palavras_chave[1] + ',' + self.palavras_chave[2]

    def salvar_arquivo(self, noticia):
        try:
            with open('base_dados.csv','a') as f:
                f.write(noticia.id+';')
                f.write(noticia.titulo+';')
                f.write(noticia.categoria+';')
                f.write(noticia.texto+';')
                f.write(noticia.palavra_chave)
                f.close()
                return 'Notícia cadastrada com sucesso !!'
        except Exception as e: #erro de entrada (falha ao abrir arquivo)
            print(e)
            return 'Erro ao cadastrar notícia'

    def buscar_noticia(self, noticia):
        try:
            with open('base_dados.csv', 'r') as f:
                f.read
                linhas = f.readlines()
                for linha in linhas:
                    linha = f.readline().split(';')
                    if linha[0] == noticia.id:
                        if linha[1] == noticia.titulo:
                            if linha[2] == noticia.categoria:
                                if linha[3] == noticia.texto:
                                    if linha[4] == noticia.palavra_chave:
                                        return Noticia(linha[0],linha[1],linha[2],linha[3],self.separa_chaves(linha[4].split(',')))
                f.close()
        except Exception as e:
            print(e)

    def valida_noticia(self):
        if len(self.texto) > 400:
            return False
        elif len(self.palavras_chave) != 3:
            return False
        return True
    
    def __str__(self):
        return f'[{self.id}] {self.titulo} - {self.categoria}'
    
    def __eq__(self, other):
        if isinstance(other, Noticia):
            return self.id == other.id
        return False
    
    def __gt__(self, other):
        return self.titulo > other.titulo