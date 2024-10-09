
#### Testes Automatizados

# Importa a biblioteca unittest para criar os testes automatizados
import unittest

# Importa a função calcular_comissao que será testada
from calculo_comissoes_pagamentos import calcular_comissao

# Cria a classe de teste que vai conter os testes automatizados para a função calcular_comissao
class TestCalculoComissao(unittest.TestCase):

    # Testa o cálculo de comissão normal (vendas físicas sem descontos)
    def test_comissao_normal(self):
        # Simula uma venda com valor de 1000 reais feita em loja física
        venda = {'Valor da Venda': 1000, 'Canal de Venda': 'Loja física'}
        # Verifica se a comissão calculada é 100 reais (10% do valor da venda)
        self.assertEqual(calcular_comissao(venda), 100)

    # Testa o cálculo de comissão para vendas online (onde há um desconto de 20% para marketing)
    def test_comissao_online(self):
        # Simula uma venda com valor de 1000 reais feita por canal online
        venda = {'Valor da Venda': 1000, 'Canal de Venda': 'Online'}
        # Verifica se a comissão calculada é 80 reais (10% do valor menos 20% para marketing)
        self.assertEqual(calcular_comissao(venda), 80)

    # Testa o cálculo de comissão onde a comissão é grande o suficiente para dedução de 10% para o gerente
    def test_comissao_com_gerente(self):
        # Simula uma venda com valor de 20.000 reais feita em loja física
        venda = {'Valor da Venda': 20000, 'Canal de Venda': 'Loja física'}
        # Verifica se a comissão calculada é 1800 reais (comissão inicial de 2000 reais menos 10% para o gerente)
        self.assertEqual(calcular_comissao(venda), 1800)

# O bloco abaixo garante que os testes sejam executados quando o arquivo for rodado diretamente
if __name__ == '__main__':
    # Executa todos os testes definidos na classe TestCalculoComissao
    unittest.main()
