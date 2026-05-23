from models.midia import Midia

class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"Reproduzindo Texto Narrado -{self.titulo}/{self.duracao}/{self.idioma}-...")
        