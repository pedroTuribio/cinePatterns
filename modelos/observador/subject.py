class Subject:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, obs):
        self._observadores.append(obs)

    def notificar(self, mensagem):
        for obs in self._observadores:
            obs.atualizar(mensagem)
