class Subject:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def notificar_observadores(self, mensagem: str):
        for observador in self._observadores:
            observador.atualizar(mensagem)
