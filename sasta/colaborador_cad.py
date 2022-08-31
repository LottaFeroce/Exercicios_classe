class Colaborador:   
    def __init__(self,cargo,pis,email,salario,reservista,dependente):
        self.cargo = cargo
        self.pis = pis
        self.email = email
        self.salario = salario
        self.reservista = reservista
        self.dependente = dependente
    #cadastrar Colaborador
    def cadastrarColaborador(self,cargo,pis,email,salario,reservista,dependente):
        self.cargo  = cargo
        cargo = input("Cargo: ")
        self.pis = pis
        pis = input("Pis: ")
        self.email = email
        email = input ("Email: ")
        self.salario = salario
        salario = input("Salario:")
        self.reservista = reservista
        reservista = input("Reservista:")
        self.dependente = dependente
        dependente = input("Dependente:")
        self.cargo  = cargo
        self.pis = pis
        self.email = email
        self.salario = salario
        self.reservista = reservista
        self.dependente = dependente
    def relatorioColaborador(self):
        print(f' Cargo: {self.cargo}\n Pis: {self.pis}\n Email: \t{self.email}')
        print(f' Salario: \t{self.salario}\n Reservista: \t{self.reservista}\n Dependente: \t{self.dependente}')

    def alterarColaborador(self,cargo,pis,email,salario,reservista,dependente):
        self.cargo  = cargo
        cargo = input("Cargo: ")
        self.pis = pis
        pis = input("Pis: ")
        self.email = email
        email = input ("Email: ")
        self.salario = salario
        salario = input("Salario:")
        self.reservista = reservista
        reservista = input("Reservista:")
        self.dependente = dependente


    def excluirColaborador(self):
        self.cargo = " "
        self.pis= " "
        self.email = " "
        self.salario = " "
        self.reservista = " "
        self.dependente = " "