from abc import ABC, abstractmethod
import os


# Funções utilitárias


def limpar_terminal():
    """Limpa a tela do terminal para uma execução mais limpa."""
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_secao(texto: str):
    """Imprime um título de seção com divisores."""
    print("\n" + "=" * 60)
    print(f"{texto.upper()}")
    print("=" * 60)

# Classes básicas


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
        print(f"Funcionário: {self.nome} | Cargo: {self.cargo}")

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
        print(f"Sessão: {self.filme.titulo} - {self.horario} (Sala {self.sala.numero})")


# Padrão Observer


class Observer(ABC):
    @abstractmethod
    def atualizar(self, mensagem: str):
        pass

class Subject:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def notificar_observadores(self, mensagem: str):
        for observador in self._observadores:
            observador.atualizar(mensagem)

class Cliente(Pessoa, Observer):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)

    def login(self):
        print(f"Cliente logado: {self.nome}")

    def comprar_ingresso(self, valor: float, metodo_pagamento):
        print(f"\n{self.nome} está comprando um ingresso...")
        metodo_pagamento.pagar(valor)

    def atualizar(self, mensagem: str):
        print(f"Notificação para {self.nome}: {mensagem}")

# Padrão Strategy: Pagamento


class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado via Pix.")

class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado no Cartão.")

class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor: float):
        print(f"Pagamento de R${valor:.2f} realizado em Dinheiro.")


# Padrão Singleton: Sistema do Cinema


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
        mensagem = f"Novo filme em cartaz: {sessao.filme.titulo} às {sessao.horario} (Sala {sessao.sala.numero})"
        print(f"\n{mensagem}")
        self.sessoes.append(sessao)
        self.notificar_observadores(mensagem)

    def listar_sessoes(self):
        titulo_secao("Sessões disponíveis")
        if not self.sessoes:
            print("Nenhuma sessão cadastrada no momento.")
        else:
            for i, sessao in enumerate(self.sessoes, start=1):
                print(f"{i}. {sessao.filme.titulo} - {sessao.horario} (Sala {sessao.sala.numero})")


# Função principal com menu interativo


def main():
    limpar_terminal()
    titulo_secao("Sistema de Cinema")

    sistema = SistemaCinema.get_instance()

    # Clientes (Observer)
    cliente1 = Cliente("Pedro", "pedro@email.com")
    cliente2 = Cliente("Mariana", "mariana@email.com")
    sistema.adicionar_observador(cliente1)
    sistema.adicionar_observador(cliente2)

    # Filmes e sessões
    filme1 = Filme("Deadpool 3", 135, "16 anos")
    filme2 = Filme("Truque de Mestre 3", 136, "18 anos")

    sala1 = Sala(1, 100)
    sala2 = Sala(2, 120)

    sessao1 = Sessao(filme1, sala1, "21:00")
    sessao2 = Sessao(filme2, sala2, "21:10")

    sistema.adicionar_sessao(sessao1)
    sistema.adicionar_sessao(sessao2)

    # MENU INTERATIVO
    while True:
        limpar_terminal()
        titulo_secao("MENU PRINCIPAL")
        print("1. Listar sessões")
        print("2. Comprar ingresso")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            sistema.listar_sessoes()
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            sistema.listar_sessoes()
            escolha = input("\nEscolha o número da sessão: ")

            try:
                escolha = int(escolha)
                sessao = sistema.sessoes[escolha - 1]
            except (ValueError, IndexError):
                print("Sessão inválida!")
                input("\nPressione ENTER para continuar...")
                continue

            titulo_secao("Forma de Pagamento")
            print("1. Pix")
            print("2. Cartão")
            print("3. Dinheiro")
            tipo_pagamento = input("\nEscolha o método de pagamento: ")

            if tipo_pagamento == "1":
                metodo = PagamentoPix()
            elif tipo_pagamento == "2":
                metodo = PagamentoCartao()
            elif tipo_pagamento == "3":
                metodo = PagamentoDinheiro()
            else:
                print("Opção inválida.")
                input("\nPressione ENTER para continuar...")
                continue

            cliente1.comprar_ingresso(35.00, metodo)
            print(f"Ingresso para '{sessao.filme.titulo}' comprado com sucesso!")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            print("\nEncerrando o sistema... até logo!")
            break
        else:
            print("Opção inválida!")
            input("\nPressione ENTER para continuar...")

# --------------------------------------------------

if __name__ == "__main__":
    main()
