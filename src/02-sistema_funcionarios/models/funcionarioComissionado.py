from models.funcionario import Funcionario
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, cpf, total_vendas, percentual_comissao):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self):
        return self.total_vendas * self.percentual_comissao