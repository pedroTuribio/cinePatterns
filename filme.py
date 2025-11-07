class Filme:
    def __init__(self, titulo: str, duracao: int, classificacao: str):
        self.titulo = titulo
        self.duracao = duracao  # em minutos
        self.classificacao = classificacao

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Duração: {self.duracao} minutos")
        print(f"Classificação: {self.classificacao}")
