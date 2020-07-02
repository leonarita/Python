from veiculo import Veiculo
from carro import Carro
# dentro do arquivo veiculo, importa a classe Veiculo

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

print(caminhao_rosa)
print(type(caminhao_rosa))

print ("\n")
print ("CAMINHÃO ROSA")
print ("Cor: ", caminhao_rosa.cor)
print ("Marca: ", caminhao_rosa.marca)
print ("Tanque: ", caminhao_rosa.tanque)

carro_azul = Carro('azul', 4, 'BMW', 30)

print ("\n")
print ("CARRO AZUL")
print ("Cor: ", carro_azul.cor)
print ("Marca: ", carro_azul.marca)
print ("Tanque: ", carro_azul.tanque)

carro_azul.abastecer (10)
print ("Tanque abastecido: ", carro_azul.tanque)

carro_azul.abastecer (70)
print ("Tanque abastecido: ", carro_azul.tanque)