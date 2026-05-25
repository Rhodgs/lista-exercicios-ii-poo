
from models.armazenador import Armazenador
from models.salvavel import Salvavel
from models.armazenadorArquivo import ArmazenadorArquivo
from models.armazenadorBanco import ArmazenadorBanco
from models.armazenadorNuvem import ArmazenadorNuvem
# "Deve trabalhar com a hierarquia baseada em ABC
def executar_salvamento_formal(armazenador: Armazenador, dado: str):
    armazenador.salvar(dado)
    if not isinstance(armazenador, Armazenador):
        # O 'raise' cria o erro físico e para a execução do script
        raise TypeError("\nerro: O objeto não herda da classe abstrata Armazenador")
# "Deve trabalhar com qualquer objeto compatível com o protocolo Salvavel"
def executar_salvamento_flexivel(objeto: Salvavel, dado: str):
    objeto.salvar(dado)

def main():
    arq = ArmazenadorArquivo()
    bd = ArmazenadorBanco()
    nuvem = ArmazenadorNuvem()

    dado_teste = "Relatorio_Financeiro_2026.pdf"
    print("\n--- TESTE 1: SALVAMENTO FLEXÍVEL (PROTOCOL) ---")
    
    # Todo mundo funciona aqui! Porque Protocol só olha para o método "salvar", não para a família da classe
    executar_salvamento_flexivel(arq, dado_teste) 
    executar_salvamento_flexivel(bd, dado_teste)  
    executar_salvamento_flexivel(nuvem, dado_teste) 

    print("\n--- TESTE 2: SALVAMENTO FORMAL (ABC) ---")
    executar_salvamento_formal(arq, dado_teste) # Funciona (é filho de Armazenador)
    executar_salvamento_formal(bd, dado_teste)  # Funciona (é filho de Armazenador)

    print("\nAtenção: Tentando salvar na nuvem usando o método formal, porem o programa vai quebrar agora!")
    # a linha abaixo vai acionar o nosso 'raise' e acionar o erro na tela, retire o "#" para testar
    
    # executar_salvamento_formal(nuvem, dado_teste)
    
# Em qual parte há contrato por herança?
# Na Parte A, com a classe abstrata Armazenador (ABC) e as filhas ArmazenadorArquivo e ArmazenadorBancp

# Em qual parte há contrato estrutural?
# Na Parte B, com o Salvavel (Protocol) e a classe livre ArmazenadorNuvem

# Qual abordagem é mais flexível?
#A abordagem Estrutural (Protocol / Duck Typing), Ela aceita qualquer classe de qualquer parte do seu sistema 
# ou até mesmo de bibliotecas externas de terceiros, desde que o objeto atenda ao requisito de 
# ter a assinatura do método solicitada

# Em qual situação ABC faz mais sentido? E em qual Protocol faz mais sentido?
# ABC faz sentido: Quando as classes precisam obrigatoriamente compartilhar atributos em comum
# Protocol faz sentido: Quando você se importa apenas com o comportamento (o que a classe faz) e não com a identidade (de quem ela é filha)
if __name__ == "__main__":
    main()
