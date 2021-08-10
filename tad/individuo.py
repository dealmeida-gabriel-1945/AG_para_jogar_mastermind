# Esta classe será a TAD (tipo abstrato de dado) para armazenar as informações de cada indivíduo
# e implementar algumas ações os quais podem ter
class Individuo:
    def __init__(self, tamanho_senha):
        self.chute = [None] * tamanho_senha
        self.avaliacao = [None] * tamanho_senha
        self.fitness = None

    def calcula_fitness(self, senha):
        for index, parte in enumerate(self.chute):
            if parte == senha[index]:
                self.avaliacao[index] = 1
            elif parte in senha:
                self.avaliacao[index] = 0.5
            else:
                self.avaliacao[index] = 0
        self.fitness = sum(self.avaliacao)
        return self.fitness

    def __str__(self):
        return f'{self.chute}'
