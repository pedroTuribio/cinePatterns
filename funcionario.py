

class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str, cargo: str):
        super().__init__(nome, email)
        self._cargo = cargo

    @property
    def cargo(self):
        return self._cargo

    def login(self):
        print(f"Funcionário logado: {self.nome} ({self.cargo})")

    def cadastrar_filme(self, titulo: str):
        print(f'Filme "{titulo}" cadastrado por {self.nome}')
