'''Classe Bichinho Virtual:Crie uma classe que modele
um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos:
Alterar Nome, Fome, Saúde e Idade; Retornar
Nome, Fome, Saúde e Idade Obs: Existe mais uma
informação que devemos levar em consideração, o
Humor do nosso tamagushi, este humor é uma
combinação entre os atributos Fome e Saúde, ou
seja, um campo calculado, então não devemos criar
um atributo para armazenar esta informação por
que ela pode ser calculada a qualquer momento.'''
from traceback import format_exc
from tamago_main import Tama
nome = input("Digite o nome do seu Tamagoshi: ")
fome = int(input("Informe o nível de saciedade: "))
saude = int(input("Informe o nível de saude: "))
idade = input("Informe a idade: ")
soma = (fome + saude)/2
if soma <=5:
    print("Mal-humor")
elif soma >=10:
    print("Bom humor")
gosh = Tama(nome,fome,saude,idade)
gosh.mostrar()