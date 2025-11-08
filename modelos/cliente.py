# modelos/cliente.py
# Classe Cliente herda de Pessoa e implementa o padrão Observer

from modelos.pessoa import Pessoa
from modelos.observador.observer import Observer

class Cliente(Pessoa, Observer):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)

    def login(self):
        print(f"Cliente logado: {self.nome}")

    def comprar_ingresso(self, valor: float, metodo_pagamento):
        print(f"{self.nome} está comprando um ingresso...")
        metodo_pagamento.pagar(valor)

    def atualizar(self, mensagem: str):
        print(f"📩 Notificação para {self.nome}: {mensagem}")
