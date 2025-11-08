

class Sessao:
    def __init__(self, filme: Filme, sala: Sala, horario: str):
        self.filme = filme
        self.sala = sala
        self.horario = horario

    def exibir_info(self):
        print(f"Sessão: {self.filme.titulo} - {self.horario} - Sala {self.sala.numero}")
