# models/cliente.py
# Classe Cliente herda de Pessoa e representa um cliente do cinema

from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)

    def login(self):
        print(f"Cliente logado: {self.nome}")

    def comprar_ingresso(self):
        print(f"{self.nome} está comprando um ingresso...")
