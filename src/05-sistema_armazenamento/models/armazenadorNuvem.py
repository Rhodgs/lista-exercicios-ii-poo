from models.salvavel import Salvavel
class ArmazenadorNuvem:
    def salvar(self, dado: str):
        print(f"[NUVEM AWS] Upload concluído: {dado}")