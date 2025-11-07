# main.py
# Testa o sistema de cinema (clientes, funcionários e sessões)

from modelos.filme import Filme
from modelos.sala import Sala
from modelos.sessao import Sessao
from modelos.sistema_cinema import SistemaCinema

def main():
    # Criação de filmes e salas
    filme1 = Filme("Vingadores: Ultimato", 181, "12 anos")
    filme2 = Filme("Homem-Aranha: Sem Volta Para Casa", 148, "12 anos")

    sala1 = Sala(1, 100)
    sala2 = Sala(2, 80)

    # Criação de sessões
    sessao1 = Sessao(filme1, sala1, "18:00")
    sessao2 = Sessao(filme2, sala2, "20:30")

    # Usando o Singleton do sistema
    sistema = SistemaCinema.get_instance()
    sistema.adicionar_sessao(sessao1)
    sistema.adicionar_sessao(sessao2)

    sistema.listar_sessoes()

if __name__ == "__main__":
    main()
