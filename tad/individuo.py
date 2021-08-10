# Esta classe será a TAD (tipo abstrato de dado) para armazenar as informações de cada indivíduo
# e implementar algumas ações os quais podem ter
class Individuo:
    def __init__(self, tamanho_senha):
        self.chute = [None] * tamanho_senha
        self.pontuacao = None
