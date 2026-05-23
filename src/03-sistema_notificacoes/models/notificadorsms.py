from models.notificador import Notificador

class NotificadorSMS(Notificador):
    def __init__(self):
        super().__init__()

    def notificar(self, mensagem):
        print(f"[SMS] Enviando torpedo para o celular... \n-> Conteúdo: {mensagem}\n")