from typing import Protocol

class Salvavel(Protocol):
    def salvar(self, dado: str) -> None:
        ...