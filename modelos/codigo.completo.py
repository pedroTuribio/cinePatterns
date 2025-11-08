from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        print(f"Nome: {self.nome} | Email: {self.email}")


class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str, cargo: str):
        super().__init__(nome, email)
        self.cargo = cargo

    def exibir_info(self):
        print(f"Funcionario: {self.nome} | Cargo: {self.cargo}")


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

    def exibir_info(self):
        print(f"Sessão: {self.filme.titulo} - {self.horario} - Sala {self.sala.numero}")


class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass


class Subject:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, mensagem: str):
        for observador in self._observadores:
            observador.atualizar(mensagem)


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


class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass


class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado via Pix ✅")


class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado no Cartão 💳")


class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado em Dinheiro 💵")


class SistemaCinema(Subject):
    _instancia = None

    def __init__(self):
        if SistemaCinema._instancia is not None:
            raise Exception("Use SistemaCinema.get_instance() para obter a instância do sistema.")
        super().__init__()
        self.sessoes = []

    @staticmethod
    def get_instance():
        if SistemaCinema._instancia is None:
            SistemaCinema._instancia = SistemaCinema()
        return SistemaCinema._instancia

    def adicionar_sessao(self, sessao: Sessao):
        self.sessoes.append(sessao)
        mensagem = f"Novo filme em cartaz: {sessao.filme.titulo} às {sessao.horario} (Sala {sessao.sala.numero})"
        print(mensagem)
        self.notificar_observadores(mensagem)

    def listar_sessoes(self):
        print("\n📅 Sessões disponíveis:")
        for sessao in self.sessoes:
            sessao.exibir_info()


def main():
    sistema = SistemaCinema.get_instance()

    cliente1 = Cliente("Pedro", "pedro@email.com")
    cliente2 = Cliente("Mariana", "mariana@email.com")

    sistema.adicionar_observador(cliente1)
    sistema.adicionar_observador(cliente2)

    filme = Filme("Deadpool 3", 135, "16 anos")
    sala = Sala(1, 100)
    sessao = Sessao(filme, sala, "21:00")

    sistema.adicionar_sessao(sessao)
    sistema.listar_sessoes()

    print("\n💳 Compras de ingressos:")
    cliente1.comprar_ingresso(35.00, PagamentoPix())
    cliente2.comprar_ingresso(35.00, PagamentoCartao())


if __name__ == "__main__":
    main()
