class CentralNotificacoes():
    def __init__(self, nome):
        self.listaNotifica = []
        self.nome = nome

    def adicionar_notificador(self, notificador):
        self.listaNotifica.append(notificador)
    def enviar_para_todos(self, mensagem):
   
        print("\nDISPARANDO NOTIFICAÇÕES EM MASSA:")
        
        for noti in self.listaNotifica:
            noti.notificar(mensagem)
