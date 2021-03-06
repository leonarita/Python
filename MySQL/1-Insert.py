# Importamos a biblioteca:
import pymysql

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='garagem', user='root', passwd='123456')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("INSERT INTO carros (placa, nome_dono) VALUES ('ABC-1234', 'Joao')")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()