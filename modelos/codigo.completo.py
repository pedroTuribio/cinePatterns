"""
Sistema de Cinema com 3 Padrões de Projeto
Padrões mantidos:
1. Observer
2. Strategy
3. Singleton
"""

from abc import ABC, abstractmethod
import os

# -----------------------------
# Funções utilitárias
# -----------------------------

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_secao(texto: str):
    print("" + "=" * 60)
    print(texto.upper())
    print("=" * 60)
# -----------------------------
# Classes básicas
# -----------------------------

class Pessoa:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

class Filme:
    def __init__(self, titulo: str, duracao: int, classificacao: str):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao

class Sala:
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade

class Sessao:
    def __init__(self, filme, sala, horario: str):
        self.filme = filme
        self.sala = sala
        self.horario = horario

# -----------------------------
# Observer
# -----------------------------

class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass

class Subject:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, obs):
        self._observadores.append(obs)

    def notificar(self, mensagem):
        for obs in self._observadores:
            obs.atualizar(mensagem)

class Cliente(Pessoa, Observer):
    def atualizar(self, mensagem: str):
        print(f"Notificação para {self.nome}: {mensagem}")

    def comprar(self, valor, metodo):
        print(f"{self.nome} está comprando...")
        metodo.pagar(valor)

# -----------------------------
# Strategy (Pagamento)
# -----------------------------

class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} via Pix.")

class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} no Cartão.")

class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} em Dinheiro.")

# -----------------------------
# Singleton: Sistema de Cinema
# -----------------------------

class SistemaCinema(Subject):
    _instancia = None

    def __init__(self):
        if SistemaCinema._instancia is not None:
            raise Exception("Use get_instance().")
        super().__init__()
        self.sessoes = []

    @staticmethod
    def get_instance():
        if SistemaCinema._instancia is None:
            SistemaCinema._instancia = SistemaCinema()
        return SistemaCinema._instancia

    def adicionar_sessao(self, s):
        msg = f"Nova sessão: {s.filme.titulo} às {s.horario}"
        print(msg)
        self.sessoes.append(s)
        self.notificar(msg)

    def listar_sessoes(self):
        titulo_secao("Sessões Disponíveis")
        for idx, s in enumerate(self.sessoes, 1):
            print(f"{idx}. {s.filme.titulo} - {s.horario}")

# -----------------------------
# Programa principal
# -----------------------------

def main():
    SistemaCinema._instancia = None
    sistema = SistemaCinema.get_instance()

    c1 = Cliente("Pedro", "pedro@email")
    sistema.adicionar_observador(c1)

    f1 = Filme("Deadpool 3", 135, "16 anos")
    sala = Sala(1, 100)
    sessao = Sessao(f1, sala, "21:00")
    sistema.adicionar_sessao(sessao)

    sistema.listar_sessoes()

    pagamento = PagamentoPix()
    c1.comprar(35.0, pagamento)

if __name__ == "__main__":
    main()
