class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.listaFuncionarios = []
    
    def adicionar_funcionario(self,funcionario):
        self.listaFuncionarios.append(funcionario)
    def listar_funcionarios(self):
        print(f"\n--- Funcionários da Empresa {self.nome} ---")
        for func in self.listaFuncionarios:
            func.mostrar_dados()
    def mostrar_folha_pagamento(self):
        total_folha = 0
        print(f"\n----- FOLHA DE PAGAMENTO: {self.nome} -----")
        
        for func in self.listaFuncionarios:
            valor_pagamento = func.calcular_pagamento()
            
            print(f"Funcionário: {func.nome} | CPF: {func.cpf} | Recebe: R$ {valor_pagamento:.2f}")
            
            
            total_folha += valor_pagamento

        print(f"VALOR TOTAL DA FOLHA: R$ {total_folha:.2f}")