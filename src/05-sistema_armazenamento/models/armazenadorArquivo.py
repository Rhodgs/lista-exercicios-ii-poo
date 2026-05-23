from models.armazenador import Armazenador

class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: str):
        print(f"[ARQUIVO LOCAL] Dado salvo no disco: {dado}")