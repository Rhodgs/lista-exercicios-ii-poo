from models.notificador import Notificador

class NotificadorEmail(Notificador):
    def __init__(self):
        super().__init__()

    def notificar(self, mensagem):
        print(f"[EMAIL] Enviando e-mail seguro... \n-> Conteúdo: {mensagem}\n")