class Conta:

    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero

        self.cpf = cpf

        self.nomeTitular = nomeTitular

        self.saldo = saldo

def depositar(self, valor):

    self.saldo += valor

def sacar(self, valor):

    self.saldo -= valor

    def gerarExtrato(self):
        print(f"numero: {self.numero} \n Nome:{self.nomeTitular}\n cpf: {self.cpf}\nsaldo: {self.saldo}")

gerarExtrato()

gerarExtrato()