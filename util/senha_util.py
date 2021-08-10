from random import randrange


def gera_senha(tamanho_senha, opcoes):
    """
    Gerar senha aleatória e sem repetições

    :param tamanho_senha -> tamanho da senha
    :param opcoes -> quais são os caracteres que podem aparecer em cada posição da senha
    :returns senha -> senha pseudo-aleatória
    """
    tamanho_opcoes = len(opcoes)
    senha = []
    for x in range(0, tamanho_senha):
        proximo_elemento = None
        while ((proximo_elemento is None) or (proximo_elemento in senha)) and (len(senha) < tamanho_senha):
            proximo_elemento = opcoes[randrange(0, tamanho_opcoes)]
        senha.append(proximo_elemento)
    return senha
