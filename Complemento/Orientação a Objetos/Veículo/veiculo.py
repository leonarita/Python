class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):  # Construtor: sempre possui o self (que equivale ao 'this' em java)
        self.cor = cor
        self.marca = marca
        self.rodas = rodas
        self.tanque = tanque

    def abastecer (self, litros):
        self.tanque += litros