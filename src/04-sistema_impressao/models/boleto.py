class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self. valor = valor

    def imprimir(self):
        print(f"[BOLETO] Código: {self.codigo} | Valor: R$ {self.valor:.2f}")        