'''Classe Macaco: Desenvolva uma classe
Macaco,que possua os atributos nome e bucho
(estômago) e pelo menos os métodos comer(),
verBucho() e digerir(). Faça um programa ou
teste interativamente, criando pelo menos dois
macacos, alimentando-os com pelo menos 3
alimentos diferentes e verificando o conteúdo do
estomago a cada refeição. Experimente fazer
com que um macaco coma o outro. É possível
criar um macaco canibal?'''
from monk_main import Macaco
nome = input("Digite o nome do macaco: ")
comida1 = input("Qual foi a primeira refeição")
comida2 = input("Qual foi a segunda refeição")
comida3 = input("Qual foi a terceira refeição")

mk = Macaco(nome,comida1,comida2,comida3)
bucho = comida1 + comida2 + comida3
VerBucho = bucho

