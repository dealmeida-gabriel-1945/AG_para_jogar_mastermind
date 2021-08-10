from util.senha_util import gera_senha
from tad.geracao import Geracao


def gera_geracao(individuos_por_geracao, tamanho_senha, opcoes):
    """
    Gerar uma série de indivíduos pseudo-aleatórios

    :param individuos_por_geracao -> quantidade de indivíduos que cada geração pode conter
    :param tamanho_senha -> tamanho que a senha possui
    :param opcoes -> opções que podem compor a senha
    :returns geração -> objeto contendo os indivíduos
    """
    geracao = Geracao()
    for num_individuo in range(0, individuos_por_geracao):
        individuo = list()
        while (len(individuo) == 0) or (individuo in geracao.individuos):
            individuo = gera_senha(tamanho_senha, opcoes)
        geracao.individuos.append(individuo)
    return geracao
