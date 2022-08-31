'''Classe TV: Faça um programa que
simule um televisor criando-o como um
objeto. O usuário deve ser capaz de
informar o número do canal e aumentar ou
diminuir o volume. Certifique-se de que o
número do canal e o nível do volume
permanecem dentro de faixas válidas.'''
from Tv import tv
canal = input("Informe qual o canal: ")
volume = input("Determine qual o volume: ")
teve = tv(canal,volume)
if canal >= 0 or canal <= 100:
    print(canal)
else:
    print("Canal invalido")
if volume == 0 or volume == 100:
    print(volume)
volume()