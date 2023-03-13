# define uma função para validar números float
def numero_valido_float(mensagem):
    while True:
        try: 
            valor_input = input(mensagem) # solicita uma entrada do usuário
            valor = float(valor_input) # converte a entrada do usuário em um número float
            return valor # retorna o número float
        except ValueError: # se ocorrer um erro de valor, informa ao usuário e continua pedindo a entrada
            print('Por Favor, insira um número valido.')

# define uma função para validar números inteiros positivos
def numero_inteiro(mensagem, maximo_valor):
    while True:
        try:
            valor_input = input(mensagem) # solicita uma entrada do usuário
            valor = int(valor_input) # converte a entrada do usuário em um número inteiro
            if valor <= 0 or valor > maximo_valor: # se o número for menor ou igual a 0 ou maior que maximo_valor, gera um erro
                raise ValueError
            return valor # retorna o número inteiro
        except ValueError: # se ocorrer um erro de valor, informa ao usuário e continua pedindo a entrada
            print('Por Favor, insira um número inteiro positivo entre 1 e 4.')

# define uma função para imprimir um traço
def tracado():
    print('-'*90)

# define uma função para calcular a porcentagem
def porcentagem(valor, porcentagem):
    valor_decimal = porcentagem / 100 # converte a porcentagem para um valor decimal
    resultado = valor * valor_decimal # calcula o valor da porcentagem
    return resultado # retorna o resultado

# solicita o preço do produto ao usuário
preco_normal = numero_valido_float('Digite o preço do produto: ')

# imprime um traço para separar as seções
tracado()

# solicita a opção de pagamento ao usuário e imprime a opção selecionada
print('OPÇÕES DE PAGAMENTO:\n\n[1]PAGAMENTO EM DINHEIRO À VISTA\n[2]PAGAMENTO COM CARTÃO DE CRÉDITO OU DÉBITO À VISTA\n[3]PAGAMENTO COM CARTÃO DE CRÉDITO PARCELADO EM 2X\n[4]PAGAMENTO COM CARTÃO DE CRÉDITO PARCELADO EM 3X\n')
opcao_de_pagamento = numero_inteiro('Selecione uma opção de pagamento: ', 4)
print('Você selecionou a opção:[',opcao_de_pagamento,']')

# imprime um traço para separar as seções
tracado()

# verifica a opção de pagamento selecionada e calcula o preço com desconto ou juros
if opcao_de_pagamento == 1:
    # calcula o preço com desconto de 10% para pagamento em dinheiro à vista
    pagamento_dinheiro_avista = porcentagem(preco_normal, 10)
    print('Você recebeu 10% de desconto nessa opção.\nValor c/ desconto:','R$',preco_normal - pagamento_dinheiro_avista,'reais')
elif opcao_de_pagamento == 2:
    pagamento_cartao_avista = porcentagem(preco_normal, 5)
    print('Você recebeu 5% de desconto.\nValor c/ desconto:','R$', preco_normal-pagamento_cartao_avista,'reais' )
elif opcao_de_pagamento == 3:
    pagamento_cartao_parcelado_2x = preco_normal
    print('Você pagara o preço normal.\nValor s/ desconto:', preco_normal - pagamento_cartao_parcelado_2x)
elif opcao_de_pagamento == 4:
    pagamento_cartao_parcelado_3x = preco_normal+(porcentagem(preco_normal, 20))
    print('Sera acrescentado 20% de juros no valor da compra .\nValor c/ juros:', pagamento_cartao_parcelado_3x)
