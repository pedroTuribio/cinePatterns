class SistemaCinema(Subject):
    _instancia = None

    def __init__(self):
        if SistemaCinema._instancia is not None:
            raise Exception("Use get_instance().")
        super().__init__()
        self.sessoes = []

    @staticmethod
    def get_instance():
        if SistemaCinema._instancia is None:
            SistemaCinema._instancia = SistemaCinema()
        return SistemaCinema._instancia

    def adicionar_sessao(self, s):
        msg = f"Nova sessão: {s.filme.titulo} às {s.horario}"
        print(msg)
        self.sessoes.append(s)
        self.notificar(msg)


    def listar_sessoes(self):
        titulo_secao("Sessões Disponíveis")
        for idx, s in enumerate(self.sessoes, 1):
            print(f"{idx}. {s.filme.titulo} - {s.horario}")
