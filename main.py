class ContaBancaria:  # BankAccount
    def __init__(self, numero, nome, saldo=0.0):
        self.numero = numero
        self.nome = nome
        
        if not isinstance(saldo, (int, float)):
            raise ValueError("Valor de saldo inicial deve ser um número")
        self.saldo = float(saldo)
        
        if type(nome) != str:
            raise ValueError("Nome do titular deve ser uma string")
        
        if self.saldo < 0:
            raise ValueError("Valor de saldo inicial deve ser maior ou igual a zero")
        
        


    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor de depósito deve ser um número")
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser maior que zero")
        self.saldo += valor
        
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor de saque deve ser um número")
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Valor de saque deve ser maior que zero")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque")
        self.saldo -= valor
        
    def consultar_saldo(self):
        return self.saldo