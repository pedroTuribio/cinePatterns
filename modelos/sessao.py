class Sessao:
    def __init__(self, filme, sala, horario: str):
        self.filme = filme
        self.sala = sala
        self.horario = horario

    def exibir_info(self):
        print(f"Sessão: {self.filme.titulo} - {self.horario} (Sala {self.sala.numero})")
