
class Plataforma():
    def __init__(self, nome):
        self.nome = nome
        self.listaMidias = []

    def adicionar_midia(self, midia):
        self.listaMidias.append(midia)
    
    def listar_midias(self):
        for midias in self.listaMidias:
            print(f"{midias.titulo}")

    def reproduzir_todas(self):
        for midias in self.listaMidias:
            midias.reproduzir()
