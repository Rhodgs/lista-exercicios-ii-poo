from models.protocoloimprimivel import Imprimivel
from models.boleto import Boleto
from models.etiqueta import Etiqueta
from models.relatoriosimples import RelatorioSimples

def processar_impressao(item: Imprimivel):
    item.imprimir()

def main():

    meu_boleto = Boleto("34191.09008 10732.565809", 150.75)
    
    minha_etiqueta = Etiqueta("Rogerio", "Rua Principal, Itacoatiara - AM")
    
    meu_relatorio = RelatorioSimples("Fechamento de Vendas Mensal")

    print("\n--- PROCESSANDO FILA DE IMPRESSÃO ---")
    

    processar_impressao(meu_boleto)
    processar_impressao(minha_etiqueta)
    processar_impressao(meu_relatorio)
    
# Onde está o contrato nesse caso?
# Na classe Imprimivel (que herda de typing.Protocol), Ela define a assinatura obrigatória (imprimir()) que
#  outros objetos precisam ter para serem aceitos pelo sistema, sem forçar uma árvore de herança

# Por que as classes podem funcionar sem herdar explicitamente do protocolo?
# Por causa do conceito de Subtipagem Estrutural, Para o interpretador do Python, não importa quem é a "classe-mãe"
#  do objeto; importa apenas se ele possui a estrutura (os métodos) que a função está pedindo

# Esse caso se aproxima mais de ABC ou de duck typing?
# Se aproxima mais de Duck Typing, Segue a regra clássica: Se tem o método imprimir(), então é Imprimivel

# Qual a principal diferença entre esse caso e o da Questão 1?
# Na Questão 1 (ABC), havia uma exigência de herança direta (subtipagem nominal), Uma mídia de vídeo só funcionava porque 
# a classe Video era "filha oficial" da superclasse Midia
# Já neste caso (Protocol), classes completamente desconexas e sem parentesco  funcionam na mesma função, apenas 
# por coincidirem no nome do método

if __name__ == "__main__":
    main()