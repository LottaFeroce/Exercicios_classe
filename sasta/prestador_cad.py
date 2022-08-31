class Prestador:
    def __init__(self,cargo,id,setor):
        self.cargo = cargo
        self.id = id
        self.setor = setor
    
    def cadastrarPrestador(self,cargo,id,setor):
        self.cargo = cargo
        self.id = id
        self.setor = setor
        cargo = input("Cargo: ")
        id = input("ID: ")
        setor = input("Setor: ")
        self.cargo = cargo
        self.id = id
        self.setor = setor

    def relatorioPrestador(self):
        print(f' Cargo: {self.cargo}\n ID: {self.id}\n Setor: \t{self.setor}')

    def alterarPrestador(self,cargo,id,setor):
        self.cargo = cargo
        self.id = id
        self.setor = setor
        cargo = input("Cargo: ")
        id = input("ID: ")
        setor = input("Setor: ")
        self.cargo = cargo
        self.id = id
        self.setor = setor

    def excluirPrestador(self):
        self.cargo = ''

        self.id = ''

        self.setor = ''
        