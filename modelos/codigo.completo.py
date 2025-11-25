"""
Sistema de Cinema com 3 Padrões de Projeto
Padrões mantidos:
1. Observer
2. Strategy
3. Singleton
"""

from abc import ABC, abstractmethod
import os


# ------------------ Funções utilitárias ------------------

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_secao(texto: str):
    print("" + "=" * 60)
    print(texto.upper())
    print("=" * 60)



# ------------------ Classes básicas ------------------
# Aqui criamos as classes que representam o cinema.

class Pessoa:
    # Classe base para clientes (HERANÇA)
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
    # Sessão junta filme + sala + horário
    def __init__(self, filme, sala, horario: str):
        self.filme = filme
        self.sala = sala
        self.horario = horario



# ------------------ Padrão OBSERVER ------------------
# Observer = objetos são avisados automaticamente de algo.

class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass


class Subject:
    # Guarda uma LISTA genérica de observadores (array de objetos diferentes)
    def __init__(self):
        self._observadores = []  # LISTA GENÉRICA

    def adicionar_observador(self, obs):
        self._observadores.append(obs)

    def notificar(self, mensagem):
        # Chama o método atualizar() de forma POLIMÓRFICA
        for obs in self._observadores:
            obs.atualizar(mensagem)


class Cliente(Pessoa, Observer):
    # HERANÇA múltipla: herda Pessoa e também Observer

    def atualizar(self, mensagem: str):
        # SOBREPOSIÇÃO (override) do método abstrato
        print(f"Notificação para {self.nome}: {mensagem}")

    def comprar(self, valor, metodo):
        # metodo é polimórfico: pode ser PIX, Cartão, Dinheiro
        print(f"{self.nome} está comprando...")
        metodo.pagar(valor)



# ------------------ Padrão STRATEGY ------------------
# Strategy = várias formas diferentes de pagamento, mas trocadas facilmente

class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass


class PagamentoPix(PagamentoStrategy):
    # POLIMORFISMO: pagar() faz coisas diferentes conforme o tipo
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} via Pix.")


class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} no Cartão.")


class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} em Dinheiro.")



# ------------------ Padrão SINGLETON ------------------
# Garante que só existe um sistema de cinema durante todo o programa.

class SistemaCinema(Subject):  # também é Subject (HERANÇA)
    _instancia = None

    def __init__(self):
        # Impede criar mais de uma instância
        if SistemaCinema._instancia is not None:
            raise Exception("Use get_instance().")
        super().__init__()
        self.sessoes = []  # Lista genérica com várias sessões

    @staticmethod
    def get_instance():
        # Retorna SEMPRE a mesma instância
        if SistemaCinema._instancia is None:
            SistemaCinema._instancia = SistemaCinema()
        return SistemaCinema._instancia

    def adicionar_sessao(self, s):
        msg = f"Nova sessão: {s.filme.titulo} às {s.horario}"
        print(msg)
        self.sessoes.append(s)  # adiciona na lista
        self.notificar(msg)  # avisa todos os clientes inscritos

    def listar_sessoes(self):
        titulo_secao("Sessões Disponíveis")
        for idx, s in enumerate(self.sessoes, 1):
            print(f"{idx}. {s.filme.titulo} - {s.horario}")



# ------------------ Programa Principal ------------------

def main():
    # Inicia o sistema como Singleton
    SistemaCinema._instancia = None
    sistema = SistemaCinema.get_instance()

    # Cliente inscrito para receber notificações
    c1 = Cliente("Pedro", "pedro@email")
    sistema.adicionar_observador(c1)

    # Criando filme, sala e sessão
    f1 = Filme("Deadpool 3", 135, "16 anos")
    sala = Sala(1, 100)
    sessao = Sessao(f1, sala, "21:00")

    # Quando adiciona sessão → clientes recebem aviso (Observer)
    sistema.adicionar_sessao(sessao)

    # Lista sessões disponíveis
    sistema.listar_sessoes()

    # Escolhe a forma de pagamento (Strategy)
    pagamento = PagamentoPix()

    # Compra é feita com polimorfismo
    c1.comprar(35.0, pagamento)


if __name__ == "__main__":
    main()

    pagamento = PagamentoPix()
    c1.comprar(35.0, pagamento)

if __name__ == "__main__":
    main()
