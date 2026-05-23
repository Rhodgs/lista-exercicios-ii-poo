from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"nome: {self.nome}, cpf: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self):
        pass