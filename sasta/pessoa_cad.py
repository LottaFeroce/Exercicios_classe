from contextlib import nullcontext


class Pessoa:
    

    def __init__(self,nome,cpf,contato,dataNascimento,estadoCivil,escolaridade):
        self.nome = nome 
        self.cpf = cpf
        self.contato = contato 
        
        self.dataNascimento = dataNascimento
        self.estadoCivil = estadoCivil
        self.escolaridade = escolaridade


    def cadastrarPessoa(self,nome,cpf,contato,dataNascimento,estadoCivil,escolaridade):
        
        self.nome = nome 
        nome = input ("Nome:")
        self.cpf = cpf
        cpf  = input ("CPF:")
        self.contato = contato
        contato = input ("Contato:")         
        self.dataNascimento = dataNascimento
        dataNascimento = input("Data de Nascimento")
        self.estadoCivil = estadoCivil
        estadoCivil = input ("Estado Civil:")
        self.escolaridade = escolaridade
        escolaridade =  input ("Escolaridade:")
        self.nome = nome 
        self.cpf = cpf
        self.contato = contato 
        self.dataNascimento = dataNascimento
        self.estadoCivil = estadoCivil
        self.escolaridade = escolaridade


    def relatorioPessoa(self) :
        print(f' Nome: {self.nome}\n CPF: {self.cpf}\n Contato: {self.contato}\n Data de Nascimento: {self.dataNascimento}\n Estado Civil: {self.estadoCivil}\n Escolaridade: {self.escolaridade}')

    def alterarPessoa(self,nome,cpf,contato,dataNascimento,estadoCivil,escolaridade):
        
        self.nome = nome 
        nome = input ("Nome:")
        self.cpf = cpf
        cpf  = input ("CPF:")
        self.contato = contato
        contato = input ("Contato:")         
        self.dataNascimento = dataNascimento
        dataNascimento = input("Data de Nascimento:")
        self.estadoCivil = estadoCivil
        estadoCivil = input ("Estado Civil:")
        self.escolaridade = escolaridade
        escolaridade =  input ("Escolaridade:")
        self.nome = nome 
        self.cpf = cpf
        self.contato = contato 
        self.dataNascimento = dataNascimento
        self.estadoCivil = estadoCivil
        self.escolaridade = escolaridade
    
    def excluirPessoa(self):
        self.nome =  ''
        self.cpf =   ''
        self.contato = ''
        self.dataNascimento = ''
        self.estadoCivil = ''
        self.escolaridade = ''
        
        