

class Pessoa(ABC):
    def __init__(self, nome: str, email: str):
        self._nome = nome
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @abstractmethod
    def login(self):
        """Método abstrato que deve ser implementado nas subclasses"""
        pass
