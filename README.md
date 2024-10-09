# Sistema de Cálculo de Comissões e Validação de Pagamentos

## Descrição

Este projeto realiza o cálculo de comissões de vendedores com base nas regras fornecidas pela empresa. Além disso, ele valida os pagamentos feitos aos vendedores, verificando se houve diferença entre o valor correto e o valor pago.

O sistema lê os dados de duas planilhas Excel: uma com os dados de vendas e outra com os pagamentos efetuados. Após o cálculo das comissões e a comparação com os pagamentos, ele gera relatórios com os resultados.

## Regras de Cálculo de Comissão

1. Cada vendedor recebe 10% sobre o valor da venda.
2. Se a venda for feita através de um canal online, 20% da comissão é destinada ao marketing.
3. Se o valor da comissão final for maior ou igual a R$ 1.500,00, 10% da comissão vai para o gerente de vendas.

### Pré-requisitos

- [Python 3.7+](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)

Instale as bibliotecas necessárias executando o seguinte comando no terminal:

pip install pandas openpyxl

## Comando para executar o código principal 

python calculo_comissoes_pagamentos.py

## Comando para executar o código de teste de automação

python -m unittest teste.py







