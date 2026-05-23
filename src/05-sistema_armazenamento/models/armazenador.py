from abc import ABC, abstractmethod

class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado: str):
        pass