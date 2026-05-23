from models.midia import Midia
from models.video import Video
from models.podcast import Podcast
from models.textonarrado import TextoNarrado  
from repositories.plataforma import Plataforma

def autoPreenchimento():
    # Preenche automaticamente Youtube, e algumas midias iniciais
    plataforma_atual = Plataforma("Youtube")

    video1 = Video("Viajando o Brasil", "30m", "1080P")
    pod1 = Podcast("NVIDIA Anti-Arte", "55.20m","BrksEDU" )
    text1 = TextoNarrado("Harry Potter e a Câmara Secreta", "10h", "PT-BR")

    plataforma_atual.adicionar_midia(video1)
    plataforma_atual.adicionar_midia(pod1)
    plataforma_atual.adicionar_midia(text1)

    return plataforma_atual

def main():
    while True:
        escolha = int(input("""
    --- Escolha uma opção: --- 
    (1) Criação Automatica (Criações inicias PreDefinidas)
    (2) Criação Manual (Criar a plataforma manualmente): """))
        if (escolha == 1):
            plataforma_atual = autoPreenchimento()
            print("\nMídias iniciais carregadas!")
            break
        elif (escolha == 2):
            plataforma_atual = Plataforma(input("Qual o nome da Plataforma?: "))
            break
        else:
            print("Opção inválida!")

    
    while True:
        opcao = int(input(f"""
--- MENU: {plataforma_atual.nome} ---
(1) Adicionar Nova Mídia
(2) Listar Mídias
(3) Reproduzir Todas
(4) Sair
Escolha: """))
        
        if opcao == 1:
            tipoMidia = int(input("Qual tipo de midia?:\n(1) Video, (2) Podcast, (3) Texto Narrado"))
            titulo = input("Título da mídia: ")
            duracao = input("Duração (ex: 30m, 2h): ")
            
            if tipoMidia == 1:
                resolucao = input("Resolucao (ex: 1080p, 4K): ")
                conv_midia = Video(titulo, duracao, resolucao)

            elif tipoMidia == 2:
                apresentador = input("Nome do apresentador: ")
                conv_midia = Podcast(titulo, duracao, apresentador)

            elif tipoMidia == 3:
                idioma = input("Idioma: ")
                conv_midia = TextoNarrado(titulo, duracao, idioma)
            else:
                print("\nTipo de mídia inválido!")
            
            plataforma_atual.adicionar_midia(conv_midia)
                     
        elif opcao == 2:
            plataforma_atual.listar_midias()
        elif opcao == 3:
            plataforma_atual.reproduzir_todas()
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            continue
# "Qual é a classe abstrata do sistema?"
# É a classe Mídia

# "Onde aparece a hierarquia?"
# na relação de herança entre as classes ao importar a 
# classe mestra que é a classe Midia, enquanto as demais são classes-filhas

# "Onde aparece o polimorfismo?"
# no método reproduzir_todas() da classe Plataforma

# "Por que Midia não deveria ser instanciada diretamente?"
# Porque Midia representa um conceito genérico e incompleto
if __name__ == "__main__":
    main()