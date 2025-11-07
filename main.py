class ContaBancaria:  # BankAccount
    def __init__(self, numero, nome, saldo=0.0):
        self.numero = numero
        self.nome = nome
        self.saldo = float(saldo)

    