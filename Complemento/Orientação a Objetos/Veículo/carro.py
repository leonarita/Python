#HERANÇA

from veiculo import Veiculo

class Carro (Veiculo):

    def __init__(self, cor, rodas, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer (self, litros):   #Vai sobrepor o método abastecer da superclasse
        if self.tanque+litros > 50:
            print ("Erro: tanque com capacidade inferior")
        else:
            self.tanque += litros