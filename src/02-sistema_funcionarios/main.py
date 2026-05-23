from models.funcionario import Funcionario
from models.funcionarioassalariado import FuncionarioAssalariado
from models.funcionariohorista import FuncionarioHorista
from models.funcionarioComissionado import FuncionarioComissionado
from repositories.empresa import Empresa

def autoPreenchimento():
    # Preenche automaticamente a Empresa e alguns funcionários iniciais
    empresa_atual = Empresa("Tech Solutions")

    func1 = FuncionarioAssalariado("Raul", "102321", 5000.0)
    func2 = FuncionarioHorista("Pedro", "987654", 160, 40.0) 
    func3 = FuncionarioComissionado("Thiago", "789123", 30000.0, 0.05)

    empresa_atual.adicionar_funcionario(func1)
    empresa_atual.adicionar_funcionario(func2)
    empresa_atual.adicionar_funcionario(func3)

    return empresa_atual

def main():
    while True:
        escolha = int(input("""
    --- Escolha uma opção: --- 
    (1) Criação Automatica (Funcionários iniciais PreDefinidos)
    (2) Criação Manual (Criar a empresa do zero): """))
        
        if (escolha == 1):
            empresa_atual = autoPreenchimento()
            print("\nFuncionários iniciais carregados!")
            break
        elif (escolha == 2):
            empresa_atual = Empresa(input("Qual o nome da Empresa?: "))
            break
        else:
            print("Opção inválida!")

    while True:
        opcao = int(input(f"""
--- MENU: {empresa_atual.nome} ---
(1) Adicionar Novo Funcionário
(2) Mostrar Folha de Pagamento
(3) Sair
Escolha: """))
        
        if opcao == 1:
            tipoFuncionario = int(input("Qual tipo de funcionário?:\n(1) Assalariado\n(2) Horista\n(3) Comissionado\nEscolha: "))
            
            if tipoFuncionario in [1, 2, 3]:
                nome = input("Nome do funcionário: ")
                cpf = input("CPF: ")
                
                if tipoFuncionario == 1:
                    salario = float(input("Salário Mensal (R$): "))
                    conv_funcionario = FuncionarioAssalariado(nome, cpf, salario)

                elif tipoFuncionario == 2:
                    horas = int(input("Horas trabalhadas: "))
                    valor_hora = float(input("Valor por hora (R$): "))
                    conv_funcionario = FuncionarioHorista(nome, cpf, horas, valor_hora)

                elif tipoFuncionario == 3:
                    vendas = float(input("Total de vendas do mês (R$): "))
                    percentual = float(input("Percentual de comissão (ex: 0.05 para 5%): "))
                    conv_funcionario = FuncionarioComissionado(nome, cpf, vendas, percentual)

                empresa_atual.adicionar_funcionario(conv_funcionario)
                print("\nFuncionário adicionado com sucesso!")
            else:
                print("\nTipo de funcionário inválido!")
                     
        elif opcao == 2:
            empresa_atual.mostrar_folha_pagamento()
            
        elif opcao == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            continue

# Qual é a superclasse da hierarquia?
# É a classe Funcionario

# Quais são as subclasses?
# Nas subclasses (classes-filhas) são: FuncionarioAssalariado, 
# FuncionarioHorista e FuncionarioComissionado 

# Onde ocorre sobrescrita?
# ocorre quando as subclasses reescrevem o método calcular_pagamento()
# A superclasse apenas declara que o método deve existir, mas cada subclasse 
# define sua própria lógica específica de cálculo

# Onde ocorre polimorfismo?
# no método mostrar_folha_pagamento() da classe Empresa
# Ao percorrer a lista de funcionários com um laço for, o sistema chama 
# f.calcular_pagamento() para todos eles de forma genérica

# Qual a vantagem de usar ABC nesse caso?
# Evita que alguém instancie a classe Funcionario diretamente,
# Obriga o desenvolvedor a implementar o método calcular_pagamento() 
# em qualquer nova subclasse que for criada
if __name__ == "__main__":
    main()