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

    def all_data(self):
      """Retorna a noticia completa no formato csv 'id;titulo;categoria;texto;palavras,-,chave'"""
      return '%s;%s;%s;%s;%s' % (self.id,self.titulo,self.categoria,self.texto,self.chave_to_str())

    def chave_to_str(self):
        """Separa as chaves de lista para string 'p1,p2,p3'"""
        return self.palavras_chave[0] + ',' + self.palavras_chave[1] + ',' + self.palavras_chave[2]

    def valida_noticia(self):
        """Verifica se o tamanho é menor que 400 e se tem as 3 palavras-chave"""
        if len(self.texto) > 400 or len(self.palavras_chave) != 3:
            return False
        return True

    def __str__(self):
        return f'[{self.id}] *{self.categoria.upper()}* {self.titulo}'

    def __eq__(self, other):
        if isinstance(other, Noticia):
            return self.id == other.id
        return False

    def __gt__(self, other):
        return self.titulo > other.titulo

    def mostrar_noticia(self):
          """Exibe a noticia"""
          string = """[%s] - %s
          Palavras-chave: %s
          %s

          %s""" % (self.id,self.categoria.upper(),self.chave_to_str(),self.titulo,self.texto)
          return string