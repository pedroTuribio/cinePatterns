# modelos/sistema_cinema.py
# Sistema principal com Singleton + Observer Pattern integrado

from modelos.sessao import Sessao
from modelos.filme import Filme
from modelos.sala import Sala
from modelos.observador.subject import Subject

class SistemaCinema(Subject):
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
        self.sessoes.append(sessao)
        mensagem = f"Novo filme em cartaz: {sessao.filme.titulo} às {sessao.horario} (Sala {sessao.sala.numero})"
        print(mensagem)
        self.notificar_observadores(mensagem)

    def listar_sessoes(self):
        print("\n📅 Sessões disponíveis:")
        for sessao in self.sessoes:
            sessao.exibir_info()
