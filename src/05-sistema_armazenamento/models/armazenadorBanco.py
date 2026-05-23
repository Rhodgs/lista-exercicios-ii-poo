from models.armazenador import Armazenador

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: str):
        print(f"[BANCO DE DADOS] Dado inserido na tabela: {dado}")