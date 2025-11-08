from modelos.filme import Filme
from modelos.sala import Sala
from modelos.sessao import Sessao
from modelos.sistema_cinema import SistemaCinema
from modelos.cliente import Cliente
from modelos.pagamento.metodos_pagamento import PagamentoPix, PagamentoCartao

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
