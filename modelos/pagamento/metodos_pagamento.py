from modelos.pagamento.pagamento_strategy import PagamentoStrategy

class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} via Pix.")

class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} no Cartão.")

class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagamento R${valor:.2f} em Dinheiro.")
