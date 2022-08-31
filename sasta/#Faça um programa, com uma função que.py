#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor 'P', se seu argumento for positio, e 'N', se seu valor for zero ou negativo
def n(n1):
    if  n1 <0:
        print("Valor N")
    elif n1 == 0:
        print("Zero")
    else:
        print("Valor P")
n(-1)
n(0)
n(1)
n(10)