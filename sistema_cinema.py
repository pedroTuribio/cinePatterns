# modelos/sistema_cinema.py
# Classe principal que gerencia o sistema de cinema (Singleton Pattern)

from modelos.sessao import Sessao
from modelos.filme import Filme
from modelos.sala import Sala

class SistemaCinema:
    _instancia = None

    def __init__(self):
        if SistemaCinema._instancia is not None:
            raise Exception("Use SistemaCinema.get_instance() para obter a instância do sistema.")
        self.sessoes = []

    @staticmethod
    def get_instance():
        if SistemaCinema._instancia is None:
            SistemaCinema._instancia = SistemaCinema()
        return SistemaCinema._instancia

    def adicionar_sessao(self, sessao: Sessao):
        self.sessoes.append(sessao)
        print(f"Sessão adicionada: {sessao.filme.titulo} às {sessao.horario} (Sala {sessao.sala.numero})")

    def listar_sessoes(self):
        print("\n📅 Sessões disponíveis:")
        for sessao in self.sessoes:
            sessao.exibir_info()
