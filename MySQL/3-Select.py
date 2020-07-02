# Importamos a biblioteca:
import pymysql

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='garagem', user='root', passwd='123456')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("SELECT * FROM carros WHERE placa = 'ABC-1234'")

# Recupera o resultado:
resultado = cursor.fetchall()

# Mostra o resultado:
print('Dono do carro: ')

for linha in resultado:
    print(linha)

print(resultado[0][0])
print(resultado[0][1])
print(resultado[0][2])

# Finaliza a conexão
conexao.close()