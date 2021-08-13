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
    """
    Essa função sorteia um novo número o qual não foi banido e nem está sendo utilizado
    :param inputs_banidos: caracteres que não serão utilizado mais pelas gerações futuras
    :param inputs_usados: caracteres que já estão sendo utilizados
    :return:
    """
    return choice([valor for valor in Params.opcoes if (valor not in inputs_banidos) and (valor not in inputs_usados)])
