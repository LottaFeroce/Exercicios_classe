'''Classe Quadrado: Crie uma classe
que modele um quadrado:

Atributos: Tamanho do lado

Métodos: Mudar valor do Lado, Retornar
valor do Lado e calcular Área;'''
class quadrado:
    def __init__(self,lado=0):
        self.lado = lado
    def lado(self):
        return self.lado
    def lado(self, n):
        def valorL(self):
            print("O valor do lado é {}".format(self.lado))
    def mudarL(self):
        novoL = input("mude o lado de {}: ".format(self.lado))
        self.lado = novoL
    def calculo(self):
        print("A área do quadrado é {:.2f}"(float(self.lado)*float(self.lado)))
    def __str__ (self):
        return ("O quadrado possui {} de lado e {:.2f} de área".format(self.lado, float(self.lado)* float(self.lado)))        
def main():
    quad = quadrado()
    lado = input("Diga o valor do lado: ")
    quad.lado = lado
    print(quad)
    quad.mudarL()
    quad.lado()
    quad.calculo()
main()