from models.funcionario import Funcionario
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, cpf, horas_trabalhadas, valor_hora):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora