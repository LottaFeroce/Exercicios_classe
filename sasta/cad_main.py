from ast import While
import os
from wsgiref.validate import validator
from login_tela import Login
from menu_pront import  menuAluno, menuColaborador, menuLogin, menuPrestador, menupronto1
from aluno_cad import Aluno
from pessoa_cad import Pessoa
from colaborador_cad import Colaborador
from prestador_cad import Prestador
prestador1 = Prestador('','','')

colaborador1 = Colaborador('','','','','','')

pessoa1 = Pessoa('','','','','','')
login1 = Login ()
menu1 = menupronto1('BEM VINDO')
Aluno1 = Aluno('','','')
login = str (input("Login: "))
senha = str (input("Senha: "))
login1.menuLogin(login,senha)
os.system('pause')
os.system('cls')
while login1.menuLogin(login,senha) == True:
    
   
    menu1 = menupronto1('BEM VINDO\n -|1| Aluno\n -|2| Colaborador\n -|3| Prestador de serviços\n -|4| Cadastrar Usuario\n -|0| sair ')
    opcao = int (input("Escolha Uma Opcão:"))
    os.system('cls')
    if opcao == 1:#Menu Aluno
        
        
        while True:
            menu1 = menupronto1("Cadastro de Aluno: ")
            menu1 = menuAluno()
            opcao = int (input("Escolha Uma Opcão:"))
            os.system('cls')
            if opcao == 1:
                menu1 = menupronto1('Cadastrar Aluno')
                Aluno1.cadastrarAluno('','','')
                pessoa1.cadastrarPessoa('','','','','','')
                os.system('pause')
                os.system('cls')
            elif opcao == 2 :
                menu1 = menupronto1('Alterar Dados')
                Aluno1.alterarAlunos('','','')
                pessoa1.alterarPessoa('','','','','','')
                print("Dados ALterados")
                os.system('pause')
                os.system('cls') 

            elif opcao == 3 :
                menu1 = menupronto1('Imprimir')
                pessoa1.relatorioPessoa()
                Aluno1.relatorioAluno()
                os.system('pause')
                os.system('cls')
                
            elif opcao == 4:
                Aluno1.excluirAluno()
                pessoa1.excluirPessoa()
                
                os.system('pause')
                os.system('cls') 

            elif opcao == 0:
                
                break
    elif opcao == 2: #Menu Colaborador
        while True:
            menu1 = menupronto1("Colaboradores: ")
            menu1 = menuColaborador()
            opcao = int (input("Escolha Uma Opcão:"))
            if opcao == 1:
                menu1 = menupronto1('Cadastrar Colaborador')
                pessoa1.cadastrarPessoa('','','','','','')
                colaborador1.cadastrarColaborador('','','','','','')
                os.system('pause')
                os.system('cls')
            elif opcao == 2:
                menu1 = menupronto1 ("Alterar Dados")
                pessoa1.alterarPessoa('','','','','','')
                colaborador1.alterarColaborador('','','','','','')
                print("Dados ALterados")
                os.system('pause')
                os.system('cls') 
            
            elif opcao == 3:
                menu1 = menupronto1('Imprimir')
                pessoa1.relatorioPessoa()
                colaborador1.relatorioColaborador()
                os.system('pause')
                os.system('cls')

            elif opcao == 4:
                pessoa1.excluirPessoa()
                colaborador1.excluirColaborador
                os.system('pause')
                os.system('cls')
            elif opcao == 0:
                
                break
    elif opcao == 3:#Menu Prestador
        while True:
            menu1 = menupronto1("Prestador: ")
            menu1 = menuPrestador()
            opcao = int (input("Escolha Uma Opcão:"))
                
            os.system('cls')
            if opcao == 1:
                menu1 = menupronto1('Cadastrar Prestador')
                pessoa1.cadastrarPessoa('','','','','','')
                prestador1.cadastrarPrestador('','','')
                os.system('pause')
                os.system('cls')
            elif opcao == 2:
                menu1 = menupronto1 ('Alterar Dados')
                pessoa1.alterarPessoa('','','','','','')
                prestador1.alterarPrestador('','','')
                os.system('pause')
                os.system('cls')
            elif opcao == 3 :
                menu1 = menupronto1('Imprimir')
                pessoa1.relatorioPessoa()
                prestador1.relatorioPrestador()
                os.system('pause')
                os.system('cls')
            
            elif opcao == 4:
                prestador1.excluirPrestador()()
                pessoa1.excluirPessoa()
                os.system('pause')
                os.system('cls')

            elif opcao == 0:
                
                break
    elif opcao == 4 :#Menu Cadastrar Login e Senha
        while True:
            menu1 = menupronto1("Cadastro de Aluno: ")
            menu1 = menuLogin()
            opcao = int (input("Escolha Uma Opcão:"))
            os.system('cls')

            while True:
                
                if opcao == 1:
                    menu1 = menupronto1('Cadastrar Login e Senha')
                    
                    login1.cadastrarlogin()
                    os.system('cls')
                    break

                elif opcao == 0:
                    os.system('cls')
                    break
                
    elif opcao == 0:#Sair do sistema
        print("Até Breve...") 
        break
    