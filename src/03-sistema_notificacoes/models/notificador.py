from abc import ABC, abstractmethod

class Notificador(ABC):
    def __init__(self):
        @abstractmethod
        def notificar(self, mensagem):
            pass