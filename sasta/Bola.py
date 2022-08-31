#Classe Bola: Crie uma classe que
#modele uma bola: Atributos: Cor, circunferência, material Métodos: trocaCor e mostraCor
class bola:
    def __init__(self,cor:str,circunferencia:int,material:str):
        self.cor = cor=input("Digite a nova Cor: ")
        self.circunferencia = circunferencia=input("Informe a circunfêrencia da bola: ")
        self.material = material=input("Declare o material da bola: ")
    def mostrar(self):
         print(f'Cor: {self.cor},Circunfêrencia {self.circunferencia},Material {self.material}')
    def trocacor(self):
        cor = cor = input("Digite a cor da bola: ")
        novac = cor
        print(novac)
    trocacor()
obj = bola("Vermelho",26,"Borracha")
obj.mostrar()
