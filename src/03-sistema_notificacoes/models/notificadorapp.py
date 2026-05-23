from models.notificador import Notificador

class NotificadorApp(Notificador):
    def __init__(self):
        super().__init__()

    def notificar(self, mensagem):
        print(f"[APP] Disparando alerta na barra de notificações... \n-> Conteúdo: {mensagem}\n")