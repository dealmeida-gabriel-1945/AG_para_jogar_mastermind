# Esta classe será a TAD (tipo abstrato de dado) para armazenar as informações de cada geração
# e implementar algumas ações a qual pode ter
class Geracao:
    def __init__(self):
        self.individuos = list()
        self.caracteres_banidos = list()
        self.numero = 1

    def __str__(self):
        str = [f'{individuo}' for individuo in self.individuos]
        return f'Geração de número {self.numero}. Indivíduos \n {str}'
