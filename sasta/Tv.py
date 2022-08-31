'''Classe TV: Faça um programa que
simule um televisor criando-o como um
objeto. O usuário deve ser capaz de
informar o número do canal e aumentar ou
diminuir o volume. Certifique-se de que o
número do canal e o nível do volume
permanecem dentro de faixas válidas.'''
class tv:
    def __init__(self, canal , volume):       
        self.canal = canal
        self.volume = volume
    def canal(self, novocanal):
        if novocanal == "+":
            print("Aumentando canal")
        elif novocanal == "-":
            print("Diminuindo canal")
    def volume(self, novovolume):
        if novovolume == "+":
            print("Aumentando o volume")
        elif novovolume == "-":
            print("Diminuindo o volume")
        self.volume = novovolume        
    
    
