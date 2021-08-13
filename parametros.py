# Caracteres que podem estar contidos na senha
# Vale salientar que um número de mais de um digito também configura um caractere (ex.: [3,3,8] != [338])
opcoes = range(100)

# Quantidade máxima de gerações que podem ser geradas para tentar alcançar a senha desejada
total_geracoes = 100

# Quantidade de indivíduos que cada geração terá
# Este valor deve ser maior ou igual a 8
individuos_por_geracao = 20

# Quantidade de caracteres que a senha gerada terá
tamanho_senha = 100

# Valor utilizado para pegar, quando se tem os indivíduos ordenados pelo fitness, os x% melhores
# Exemplo: porcentagem_para_selecionar = 50
# individuos_por_geracao = 8
# Geração ordenada por fitness -> [x1, x2, x3, x4, x5, x6, x7, x8, x9,..., xn]
# O vetor resultante seria com o valor abaixo seria -> [x1, x2, x3, ..., xn/2]
porcentagem_para_selecionar = 50
