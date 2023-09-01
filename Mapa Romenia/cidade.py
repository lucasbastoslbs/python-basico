class Cidade:
    nome : str
    estimativa: int

    def __init__(self, nome, estimativa):
        self.nome = nome
        self.estimativa = estimativa

    def __str__(self):
        return f'{self.nome}. Custo estimado: {self.estimativa}.'