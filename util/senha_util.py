from random import randrange
import parametros as Params
from random import choice


def gera_senha():
    """
    Gerar senha aleatória e sem repetições

    :returns senha: senha pseudo-aleatória
    """
    tamanho_opcoes = len(Params.opcoes)
    senha = []
    for x in range(0, Params.tamanho_senha):
        proximo_elemento = None
        while ((proximo_elemento is None) or (proximo_elemento in senha)) and (len(senha) < Params.tamanho_senha):
            proximo_elemento = Params.opcoes[randrange(0, tamanho_opcoes)]
        senha.append(proximo_elemento)
    return senha


def gera_caractere_aleatorio_nao_banido_e_nao_usado(inputs_banidos, inputs_usados):
    input_selecionado = None
    while (input_selecionado is None) or (input_selecionado in inputs_banidos) or (input_selecionado in inputs_usados):
        input_selecionado = choice(Params.opcoes)
    return input_selecionado