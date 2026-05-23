from models.notificador import Notificador
from models.notificadorapp import NotificadorApp
from models.notificadoremail import NotificadorEmail
from models.notificadorsms import NotificadorSMS
from repositories.centralnotificacoes import CentralNotificacoes


def autoPreenchimento():
    # Preenche automaticamente a central e alguns funcionários iniciais
    central_atual = CentralNotificacoes("Notificações")

    canal_email = NotificadorEmail()
    canal_sms = NotificadorSMS()
    canal_push = NotificadorApp()

    central_atual.adicionar_notificador(canal_email)
    central_atual.adicionar_notificador(canal_sms)
    central_atual.adicionar_notificador(canal_push)

    return central_atual

def main():
    while True:
        escolha = int(input("""
    --- Escolha uma opção: --- 
    (1) Criação Automatica (Cadastrar canais predefinidos)
    (2) Criação Manual (Criar central vazia): """))
        
        if (escolha == 1):
            central_atual = autoPreenchimento()
            print("\nCentral configurada com todos os canais!")
            break
        elif (escolha == 2):
            central_atual = CentralNotificacoes(input("Qual o nome da Central?: "))
            print(f"\nCentral {central_atual.nome} criada!")
            break
        else:
            print("Opção inválida!")

    while True:
        opcao = int(input(f"""
--- MENU DA CENTRAL ---
(1) Adicionar Novo Canal Manualmente
(2) Enviar Mensagem para Todos
(3) Sair
Escolha: """))
        
        if opcao == 1:
            tipoCanal = int(input("Qual tipo de canal?\n(1) Email\n(2) SMS\n(3) App\nEscolha: "))
            
            if tipoCanal in [1, 2, 3]:
                
                
                if tipoCanal == 1:
                    novo_canal = NotificadorEmail()
                elif tipoCanal == 2:
                    novo_canal = NotificadorSMS()
                elif tipoCanal == 3:
                    novo_canal = NotificadorApp()

                central_atual. adicionar_notificador(novo_canal)
                print("\n Canal adicionado com sucesso!")
                     
        elif opcao == 2:
            mensagem = input("\nDigite a mensagem para disparar: ")
            central_atual.enviar_para_todos(mensagem)
        elif opcao == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            continue

# Qual classe representa o contrato formal?
# A classe abstrata Notificador, pois ela define a regra e o método obrigatório que todas as outras classes devem seguir

# Onde há polimorfismo?
# No método enviar_notificacao_geral() da CentralNotificacoes. A linha canal.notificar() chama o mesmo método, mas o Python decide na hora se vai rodar o código de Email, SMS ou Push

# Por que faz sentido usar ABC nesse caso?
# Para garantir o padrão do sistema e evitar erros, impedindo que alguém instancie 
# uma notificação "genérica" (já que toda notificação real precisa de um canal específico)

# O que aconteceria se uma subclasse de Notificador não implementasse notificar()?
# O Python bloqueia a criação do objeto e dá um erro (TypeError) logo na inicialização, 
# impedindo que um código incompleto rode

if __name__ == "__main__":
    main()