from util.senha_util import gera_senha
from util.geracao_util import gera_geracao, executa_crossover_e_mutacoes_em_geracao
import parametros as Params


def run():
    # Senha que deverá ser descoberta
    senha = gera_senha()
    print(f'\n\nSenha para ser descoberta: {senha}\n\n')
    # Flag que mostra se a senha foi, ou não, descoberta por algum indivíduo
    achou_senha = False

    # Geração atual
    geracao_atual = gera_geracao(senha)

    # Nesse while será executado todas as iterações necessárias para os crossovers e mutations
    while (geracao_atual.numero <= Params.total_geracoes) and (not achou_senha):
        print(geracao_atual)

        # Verifica se a senha foi encontrada
        if senha in [individuo.chute for individuo in geracao_atual.individuos]:
            achou_senha = True
        else:
            executa_crossover_e_mutacoes_em_geracao(geracao_atual, senha)
            geracao_atual.numero += 1

    # Prints da finalização da execução
    print('\n\n\n\n')
    if achou_senha:
        print(f'achou a senha na geração {geracao_atual.numero}')
        # print(f'Geração {geracao}')
        print('Individuos que acertaram')
        for index, individuo in enumerate(geracao_atual.individuos):
            if individuo == senha:
                print(f'{index}) {individuo}')
    else:
        print('Não foi encontrada a senha :(')


if __name__ == '__main__':
    run()

