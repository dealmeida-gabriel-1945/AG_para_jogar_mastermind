from util.senha_util import gera_senha, gera_caractere_aleatorio_nao_banido_e_nao_usado
from tad.geracao import Geracao
from tad.individuo import Individuo
import parametros as Params
from random import shuffle, choice


def gera_geracao(senha):
    """
    Gerar uma série de indivíduos pseudo-aleatórios

    :param senha: senha para ser descober, servirá para já calcular o fitness do individuo
    :returns geração: objeto contendo os indivíduos
    """
    geracao = Geracao()
    for num_individuo in range(0, Params.individuos_por_geracao):
        chute = list()
        while (len(chute) == 0) or (chute in geracao.individuos):
            chute = gera_senha()
        individuo = Individuo(Params.tamanho_senha)
        individuo.chute = chute
        individuo.calcula_fitness(senha)
        geracao.individuos.append(individuo)
    return geracao


def executa_crossover_e_mutacoes_em_geracao(geracao_atual, senha):
    """
    Esta função executa o crossover e as mutações (caso necessário) nos melhores individuos da geração atual
    :param geracao_atual: geração a qual sofrerá crossover e mutações (caso necessário)
    :param senha: senha que deve ser descoberta e será utilizada para calcular o fitness de cada novo individuo
    :return:
    """
    novos_individuos = list()
    melhores_individuos = geracao_atual.melhores_individuos()

    for progenitor_1 in melhores_individuos:
        for progenitor_2 in melhores_individuos:
            if progenitor_1 != progenitor_2:
                novos_individuos.append(executa_crossover_e_mutacoes_em_individuos(progenitor_1, progenitor_2, senha, geracao_atual.caracteres_banidos))

    geracao_atual.individuos = novos_individuos
    geracao_atual.individuos = geracao_atual.melhores_individuos(com_porcentagem_para_selecionar=False)[:Params.individuos_por_geracao]


def executa_crossover_e_mutacoes_em_individuos(progenitor_1, progenitor_2, senha, caracteres_banidos):
    """
    Esta função executa o crossover entre os progenitores, priorizando os acertos de cada um e mutando onde não há acertos
    :param progenitor_1: indivíduo que que terá os acertos priorizados
    :param progenitor_2: indivíduo que que terá os acertos priorizados após o progenitor_1
    :param senha: senha para ser descoberta
    :param caracteres_banidos: caraceters que não podem ser escolhidos
    :return: novo individuo
    """
    novo_individuo = Individuo(Params.tamanho_senha)
    for index in range(len(progenitor_1.chute)):

        for index, avaliacao in enumerate(progenitor_1.avaliacao):
            if avaliacao == 0:
                caracteres_banidos.append(progenitor_1.chute[index])

        for index, avaliacao in enumerate(progenitor_2.avaliacao):
            if avaliacao == 0:
                caracteres_banidos.append(progenitor_2.chute[index])

        aplicar_logica_onde_ha_pontuacao_1(novo_individuo, progenitor_1, progenitor_2)

        indices_para_embaralhar = aplicar_logica_onde_ha_pontuacao_0dot5(novo_individuo, progenitor_1, progenitor_2)

        aplica_mutacoes(novo_individuo, indices_para_embaralhar, caracteres_banidos)

        novo_individuo.calcula_fitness(senha)

        return novo_individuo


def aplicar_logica_onde_ha_pontuacao_1(novo_individuo, progenitor_1, progenitor_2):
    """
    Essa função é responsável por passar todos os caracteres que recebeream feedback 1, tanto no progenitor 1 tanto no 2,
    para o filho
    :param novo_individuo: o indivíduo que está sendo "montado" (filho)
    :param progenitor_1: primeiro progenitor
    :param progenitor_2: segundo progenitor
    """
    for index, veridito in enumerate(progenitor_1.avaliacao):
        if veridito == 1:
            novo_individuo.chute[index] = progenitor_1.chute[index]

    for index, veridito in enumerate(progenitor_2.avaliacao):
        if veridito == 1:
            novo_individuo.chute[index] = progenitor_2.chute[index]


def aplicar_logica_onde_ha_pontuacao_0dot5(novo_individuo, progenitor_1, progenitor_2):
    """
    Esta função realiza a passagem dos caracteres que receberam feedback 0.5, tanto no progenitor 1 tanto no 2,
    mas priorizando a não repetição de elementos dentro do indivíduo.
    Para cada valor passado dos pais para o filho é adicionado o valor de seu indice dentro do vetor que será retornado
    e, posteriormente, utilizado para realização de um embaralhamento.
    :param novo_individuo: o indivíduo que está sendo "montado" (filho)
    :param progenitor_1: primeiro progenitor
    :param progenitor_2: segundo progenitor
    :return: lista de indices a serem embaralhados dentro do novo_individuo
    """
    indices_para_embaralhar = list()
    for index in range(len(progenitor_1.avaliacao)):
        if progenitor_1.avaliacao[index] != progenitor_2.avaliacao[index]:
            if progenitor_1.avaliacao[index] == 0.5 and progenitor_2.avaliacao[index] == 0 and progenitor_1.chute[index] not in novo_individuo.chute:
                novo_individuo.chute[index] = progenitor_1.chute[index]
                indices_para_embaralhar.append(index)
            elif progenitor_2.avaliacao[index] == 0.5 and progenitor_1.avaliacao[index] == 0 and progenitor_2.chute[index] not in novo_individuo.chute:
                novo_individuo.chute[index] = progenitor_2.chute[index]
                indices_para_embaralhar.append(index)

        elif (progenitor_1.avaliacao[index] == progenitor_2.avaliacao[index]) and (progenitor_1.avaliacao[index] == 0.5):
            if progenitor_1.chute[index] not in novo_individuo.chute:
                novo_individuo.chute[index] = progenitor_1.chute[index]
                indices_para_embaralhar.append(index)
            elif progenitor_2.chute[index] not in novo_individuo.chute:
                novo_individuo.chute[index] = progenitor_2.chute[index]
                indices_para_embaralhar.append(index)
    return indices_para_embaralhar


def aplica_mutacoes(novo_individuo, indices_para_embaralhar, caracteres_banidos):
    """
    Esse método realiza, caso for necessário, as mutações de embaralhamento de valores que receberam feedback 0.5
    e a de sorteio de novos valores não utilizados e não banidos.
    :param novo_individuo: o indivíduo que está sendo "montado" (filho)
    :param indices_para_embaralhar: lista de indices que pertence ao novo_individuo que devem ser embaralhados
    :param caracteres_banidos: lista de caracteres banidos, ou seja, não serão uma opção para futuros individuos
    """
    # Caso ainda tenha Nones no novo individuo ou , ocorre a mutação
    if len(indices_para_embaralhar) != 0:
        realiza_mutacao_embaralhar_chutes_com_avaliacao_0dot5(novo_individuo, indices_para_embaralhar)
    if None in novo_individuo.chute:
        realiza_mutacao_avaliacao_0(novo_individuo, caracteres_banidos)


def realiza_mutacao_avaliacao_0(novo_individuo, caracteres_banidos):
    """
    Essa função, para cada posição do novo indivíduo, é sorteado um novo valor não utilizado e não banido.
    :param novo_individuo: o indivíduo que está sendo "montado" (filho)
    :param caracteres_banidos: lista de caracteres banidos, ou seja, não serão uma opção para futuros individuos
    """
    for index, valor in enumerate(novo_individuo.chute):
        if valor is None:
            novo_individuo.chute[index] = gera_caractere_aleatorio_nao_banido_e_nao_usado(caracteres_banidos, novo_individuo.chute)


def realiza_mutacao_embaralhar_chutes_com_avaliacao_0dot5(novo_individuo, indices_para_embaralhar):
    """
    Esta função realiza a mutação para nos valores que receberam feedback 0.5, que consiste em embaralhar, dentro do
    próprio indivíduo tais valores.
    :param novo_individuo: o indivíduo que está sendo "montado" (filho)
    :param indices_para_embaralhar: lista de indices que pertence ao novo_individuo que devem ser embaralhados
    """
    valores_dos_indices_para_embaralhar = [novo_individuo.chute[indice] for indice in indices_para_embaralhar]
    for indice in indices_para_embaralhar:
        novo_individuo.chute[indice] = None
    while len(indices_para_embaralhar) > 0:
        index_escolhido = choice(indices_para_embaralhar)
        valor_escolhido = choice(valores_dos_indices_para_embaralhar)
        indices_para_embaralhar = [indice for indice in indices_para_embaralhar if indice != index_escolhido]
        valores_dos_indices_para_embaralhar = [
            valor
            for valor in valores_dos_indices_para_embaralhar
            if valor != valor_escolhido
        ]
        novo_individuo.chute[index_escolhido] = valor_escolhido
