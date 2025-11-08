from modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str, cargo: str):
        super().__init__(nome, email)
        self.cargo = cargo

    def exibir_info(self):
        print(f"Funcionario: {self.nome} | Cargo: {self.cargo}")
