           

                          ####### VERSÃO OTIMIZADA #########


import pandas as pd

# Função para calcular a comissão com base nas regras fornecidas pela empresa
def calcular_comissao(row):
    # 10% de comissão sobre o valor da venda
    comissao = row['Valor da Venda'] * 0.10
    
    # Se a venda for por canal online, 20% da comissão vai para o marketing
    if row['Canal de Venda'] == 'Online':
        comissao *= 0.80  # O vendedor fica com 80% da comissão
    
    # Se a comissão for maior ou igual a 1500, 10% vai para o gerente de vendas
    if comissao >= 1500:
        comissao *= 0.90  # O vendedor fica com 90% da comissão

    return comissao

# Carrega a planilha de vendas, que está na aba "Vendas" do arquivo Excel
vendas = pd.read_excel('Vendas.xlsx', sheet_name='Vendas')

# Remove o símbolo de moeda (R$), remove vírgulas e converte os valores para float
vendas['Valor da Venda'] = vendas['Valor da Venda'].replace({r'R\$': '', r'\.': '', ',': '.'}, regex=True).astype(float)

# Aplica a função de cálculo de comissão para cada venda e armazena o resultado
vendas['Comissão Calculada'] = vendas.apply(calcular_comissao, axis=1)

# O valor final que o vendedor vai receber é a comissão calculada
vendas['Valor a Pagar ao Vendedor'] = vendas['Comissão Calculada']

# Exibe as comissões calculadas na tela (opcional)
print("Tabela com as comissões calculadas:")
print(vendas[['Nome do Vendedor', 'Valor da Venda', 'Comissão Calculada', 'Valor a Pagar ao Vendedor']])

# Salva a tabela de comissões calculadas em um arquivo Excel para consulta futura
vendas.to_excel('comissoes_calculadas.xlsx', index=False)

# Carrega a planilha de pagamentos, que está na aba "Pagamentos"
pagamentos = pd.read_excel('Vendas.xlsx', sheet_name='Pagamentos')

# Remove o símbolo de moeda (R$), remove vírgulas e converte os valores para float
pagamentos['Comissão'] = pagamentos['Comissão'].replace({r'R\$': '', r'\.': '', ',': '.'}, regex=True).astype(float)

# Mescla as duas tabelas (vendas e pagamentos) usando o nome do vendedor como referência
comparacao = pd.merge(vendas, pagamentos, on='Nome do Vendedor')

# Calcula a diferença entre o valor pago e o valor que deveria ter sido pago
comparacao['Diferença'] = comparacao['Comissão'] - comparacao['Valor a Pagar ao Vendedor']

# Filtra os vendedores que receberam valores incorretos
pagamentos_incorretos = comparacao[comparacao['Diferença'] != 0]

# Exibe os pagamentos incorretos na tela (opcional)
print("Pagamentos incorretos:")
print(pagamentos_incorretos[['Nome do Vendedor', 'Comissão', 'Valor a Pagar ao Vendedor', 'Diferença']])

# Salva os pagamentos incorretos em um novo arquivo Excel
pagamentos_incorretos.to_excel('pagamentos_incorretos.xlsx', index=False)


              
                      ###### VERSÃO SIMPLIFICADA ######

                      
# import pandas as pd

# # Função simples para calcular a comissão
# def calcular_comissao(row):
#     comissao = row['Valor da Venda'] * 0.10  # 10% de comissão
    
#     if row['Canal de Venda'] == 'Online':
#         comissao *= 0.80  # O vendedor fica com 80% da comissão se for venda online
    
#     if comissao >= 1500:
#         comissao *= 0.90  # Se a comissão for maior ou igual a 1500, 10% vai para o gerente
    
#     return comissao

# # Ler a planilha de vendas (primeira aba)
# vendas = pd.read_excel('Vendas.xlsx', sheet_name='Vendas')

# # Converte a coluna 'Valor da Venda' para números (float) para evitar problemas com cálculos
# vendas['Valor da Venda'] = vendas['Valor da Venda'].astype(float)

# # Aplica a função de calcular comissão
# vendas['Comissão Calculada'] = vendas.apply(calcular_comissao, axis=1)

# # Calcula o valor final a pagar ao vendedor
# vendas['Valor a Pagar ao Vendedor'] = vendas['Comissão Calculada']

# # Exibe as comissões calculadas
# print("Comissões calculadas:")
# print(vendas[['Nome do Vendedor', 'Valor da Venda', 'Comissão Calculada', 'Valor a Pagar ao Vendedor']])

# # Salva as comissões calculadas em um novo arquivo
# vendas.to_excel('comissoes_calculadas.xlsx', index=False)

# # Ler a planilha de pagamentos (segunda aba)
# pagamentos = pd.read_excel('Vendas.xlsx', sheet_name='Pagamentos')

# # Garante que os valores da comissão também sejam números
# pagamentos['Comissão'] = pagamentos['Comissão'].astype(float)

# # Mescla as tabelas de vendas e pagamentos
# comparacao = pd.merge(vendas, pagamentos, on='Nome do Vendedor')

# # Calcula a diferença entre o valor pago e o valor correto
# comparacao['Diferença'] = comparacao['Comissão'] - comparacao['Valor a Pagar ao Vendedor']

# # Filtra os pagamentos incorretos
# pagamentos_incorretos = comparacao[comparacao['Diferença'] != 0]

# # Exibe os pagamentos incorretos
# print("Pagamentos incorretos:")
# print(pagamentos_incorretos[['Nome do Vendedor', 'Comissão', 'Valor a Pagar ao Vendedor', 'Diferença']])

# # Salva os resultados dos pagamentos incorretos em um novo arquivo
# pagamentos_incorretos.to_excel('pagamentos_incorretos.xlsx', index=False)
