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
