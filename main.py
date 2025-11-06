from models.cliente import Cliente
from models.funcionario import Funcionario

def main():
    cliente1 = Cliente("Pedro", "pedro@email.com")
    funcionario1 = Funcionario("Mariana", "mariana@cinema.com", "Gerente")

    cliente1.login()
    cliente1.comprar_ingresso()

    funcionario1.login()
    funcionario1.cadastrar_filme("Homem-Aranha: Além do Aranhaverso")

if __name__ == "__main__":
    main()
