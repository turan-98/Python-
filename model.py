#  connect() cria uma conexão MySQL e retorna
# um objeto de conexão  MySQLConnection object.

import mysql.connector
from mysql.connector import errorcode

config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'bank',
    'raise_on_warnings':True
}
try:
    cnx = mysql.connector.connect(**config)
    # 'raise_on_warnings' mensagens de erro
    # criando conexão
    # connect(**config) passando argumentos em um dicionario
    #usando **

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
       print('Algo esta errado com o nome de usuario e senha')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database não existe")
    else:
        print(err)
else:
    print('Deu certo')
    cnx.close()