from abc import ABC, abstractmethod 

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        print(f"titulo {self.titulo}, duracao {self.duracao}")
    
    @abstractmethod
    def reproduzir(self):
        pass
