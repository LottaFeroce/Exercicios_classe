class pessoa:
    def __init__(self,nome:str,idade:int,peso:float): #nome : -> dois pontos = tipo
        self.nome = nome = input("Digite o nome: ")
        self.idade = idade = input("Digite a Idade: ")
        self.peso = peso = input("Digite o peso: ")
    def mostrar(self):
        print(f'nome: {self.nome},idade {self.idade}, peso {self.peso}')
    def cadastrar(pessoas):
        nome = input()
    def listar(pessoas):
        for pessoa in pessoas:
            print(f'nome: {self.nome},email {self.email}')
    def envelhecer(self):   
        if self.idade < 21:
            self.idade +=1
    def cresver(self,peso):
            self.peso +=2
    def mostrar(self):
            print(f'Nome:{self.nome},idade {self.idade} anos, peso {self.peso} Kg')
obj = pessoa("Will",25, 70.5)
obj.mostrar()
obj.envelhecer()
obj.mostrar()