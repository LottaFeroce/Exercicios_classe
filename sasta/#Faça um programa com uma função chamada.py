#Faça um programa com uma função chamada somaIposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
#que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas valor*imposto/100
def somaimposto(imposto,custo):
    valor = custo
    imposto = valor*(imposto/100)
    novo_v = valor+(valor*imposto) 
    print("Novo valor",novo_v)
somaimposto(15,25)