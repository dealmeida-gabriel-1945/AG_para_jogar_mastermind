from util.senha_util import gera_senha
from tad.geracao import Geracao
from tad.individuo import Individuo


def gera_geracao(individuos_por_geracao, tamanho_senha, opcoes, senha):
    """
    Gerar uma série de indivíduos pseudo-aleatórios

    :param individuos_por_geracao -> quantidade de indivíduos que cada geração pode conter
    :param tamanho_senha -> tamanho que a senha possui
    :param opcoes -> opções que podem compor a senha
    :param senha -> senha para ser descober, servirá para já calcular o fitness do individuo
    :returns geração -> objeto contendo os indivíduos
    """
    geracao = Geracao()
    for num_individuo in range(0, individuos_por_geracao):
        chute = list()
        while (len(chute) == 0) or (chute in geracao.individuos):
            chute = gera_senha(tamanho_senha, opcoes)
        individuo = Individuo(tamanho_senha)
        individuo.chute = chute
        individuo.calcula_fitness(senha)
        geracao.individuos.append(individuo)
    return geracao
