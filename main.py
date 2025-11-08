
def main():
    # Sistema Singleton
    sistema = SistemaCinema.get_instance()

    # Criação de clientes e inscrição para notificações
    cliente1 = Cliente("Pedro", "pedro@email.com")
    cliente2 = Cliente("Mariana", "mariana@email.com")

    sistema.adicionar_observador(cliente1)
    sistema.adicionar_observador(cliente2)

    # Criação de filmes, salas e sessões
    filme = Filme("Deadpool 3", 135, "16 anos")
    sala = Sala(1, 100)
    sessao = Sessao(filme, sala, "21:00")

    sistema.adicionar_sessao(sessao)
    sistema.listar_sessoes()

    # Clientes compram ingresso com diferentes estratégias de pagamento
    print("\n💳 Compras de ingressos:")
    cliente1.comprar_ingresso(35.00, PagamentoPix())
    cliente2.comprar_ingresso(35.00, PagamentoCartao())

if __name__ == "__main__":
    main()
