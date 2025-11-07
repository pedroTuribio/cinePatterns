class Sala:
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade

    def exibir_info(self):
        print(f"Sala {self.numero} - Capacidade: {self.capacidade} lugares")
