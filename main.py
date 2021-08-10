from util.senha_util import gera_senha
from util.geracao_util import gera_geracao
import parametros as Params


def run():
    # Senha que deverá ser descoberta
    senha = gera_senha(Params.tamanho_senha, Params.opcoes)
    print(f'\n\nSenha para ser descoberta: {senha}\n\n')
    # Contador de gerações criadas
    cont_geracao = 1
    # Flag que mostra se a senha foi, ou não, descoberta por algum indivíduo
    achou_senha = False

    # Geração atual
    geracao_atual = gera_geracao(Params.individuos_por_geracao, Params.tamanho_senha, Params.opcoes, senha)

    print(geracao_atual)
    print([individuo.fitness for individuo in geracao_atual.individuos])


if __name__ == '__main__':
    run()
