import os
from Alterac import alt 
from cadstr import cadastro
from relat import relat

while True:
    op = int(input("  Escolha qual operação será realizada:\n1-Cadastro de Clientes\n2-Alteração de Cadastro de Clientes\n3-Relatório de Clientes\n4-Sair\n Digite a Opção desejada: "))
    if op == 1:
        os.system("cls")
        cadastro()
    elif op ==2:
        os.system("cls")
        alt()
    elif op == 3:
        os.system()
        relat()
        print(nome,email,fone,cpf,endere)
    elif op == 4:
        break