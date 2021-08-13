import parametros as Params


# Esta classe será a TAD (tipo abstrato de dado) para armazenar as informações de cada geração
# e implementar algumas ações a qual pode ter
class Geracao:
    def __init__(self):
        self.individuos = list()
        self.caracteres_banidos = list()
        self.numero = 1

    def __str__(self):
        """
        Função string utilizada nos prints
        :return:
        """
        str = [f'{individuo}' for individuo in self.individuos]
        return f'Geração de número {self.numero}. {len(self.individuos)} indivíduos \n {str}'

    def melhores_individuos(self, com_porcentagem_para_selecionar=True):
        """
        Ordena e retorna a quantidade certa dos melhores individuos da geração
        :return: a quantidade certa dos melhores individuos da geração
        """
        individuos_ordenados = sorted(self.individuos, reverse=True, key=lambda individuo: individuo.fitness)
        if com_porcentagem_para_selecionar:
            return individuos_ordenados[
                   :int((Params.individuos_por_geracao * Params.porcentagem_para_selecionar) / 100)]
        return individuos_ordenados
