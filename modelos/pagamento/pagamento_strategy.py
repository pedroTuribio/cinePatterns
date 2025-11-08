# modelos/pagamento/metodos_pagamento.py
# Implementações concretas das estratégias de pagamento

from modelos.pagamento.pagamento_strategy import PagamentoStrategy

class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado via Pix ✅")

class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado no Cartão 💳")

class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado em Dinheiro 💵")
