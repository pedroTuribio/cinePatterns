from modelos.sessao import Sessao
from modelos.filme import Filme
from modelos.sala import Sala
from modelos.observador.subject import Subject

_instancia = None

    def __init__(self):
        if SistemaCinema._instancia is not None:
            raise Exception("Use SistemaCinema.get_instance() para obter a instância do sistema.")
        super().__init__()
        self.sessoes = []

    @staticmethod
    def get_instance():
        if SistemaCinema._instancia is None:
            SistemaCinema._instancia = SistemaCinema()
        return SistemaCinema._instancia

    def adicionar_sessao(self, sessao: Sessao):
        mensagem = f"Novo filme em cartaz: {sessao.filme.titulo} às {sessao.horario} (Sala {sessao.sala.numero})"
        print(f"\n{mensagem}")
        self.sessoes.append(sessao)
        self.notificar_observadores(mensagem)

    def listar_sessoes(self):
        titulo_secao("Sessões disponíveis")
        if not self.sessoes:
            print("Nenhuma sessão cadastrada no momento.")
        else:
            for i, sessao in enumerate(self.sessoes, start=1):
                print(f"{i}. {sessao.filme.titulo} - {sessao.horario} (Sala {sessao.sala.numero})")
