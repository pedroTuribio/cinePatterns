  def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        print(f"Nome: {self.nome} | Email: {self.email}")
