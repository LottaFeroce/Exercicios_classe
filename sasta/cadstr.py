class cliente:
    def __init__(self,nome:str,email:str,fone:int,cpf:int,endere:str): #nome : -> dois pontos = tipo
        self.nome = nome=input("Digite o nome: ")
        self.email = email=input("Digite o email: ")
        self.fone = fone=input("Digite o telefone: ")
        self.cpf = cpf=input("Digite o cpf: ")
        self.endere = endere=input("Digite o endereço: ")
    def mostrar(self):
        print(f'nome: {self.nome},email {self.email},fone {self.fone},cpf {self.cpf},endere {self.endere}')
    def cadastrar(pessoas):
        nome = input()
    def listar(pessoas):
        for pessoa in pessoas:
            print(f'nome: {self.nome},email {self.email},fone {self.fone},cpf {self.cpf},endere {self.endere}')
obj = cliente("Will","Willsmith@hh",239247,222888983,"Rua")
obj.mostrar()
'''def envelhecer(self):
        if self.idade< 21:
            self.idade +=1
        def cresver(self,altura):
            self.altura +=2
        def mostrar(self):
            print(f'Nome:{self.nome},idade {self.idade}anos,peso {self.peso}kg,altura{self.altura}cm)
obj = pessoa ("Ed",20,33,123)
obj.envelhecer()
obj>mostrar()'''
        #'''nome = input("Digite o Nome: ")
        #email = input("Digite o E-mail: ")
        #fone = input("Digite o Telefone: ")
        #cpf = input("Digite o Cpf : ")
        #endere = input("Digite o Endereço : ")'''

