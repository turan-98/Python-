
# coding: utf-8

# In[28]:


import mysql.connector
from mysql.connector import errorcode


nome_usr = input("Digite o seu nome: ")
tel_usr = input("Digite o seu telefone: ")
adress_usr = input("Digite o seu endereco: ")
bairro_usr = input("Digite o seu bairro: ")
num_usr = int(input("Digite o numero da casa: "))


def insert_user(nome,tel,adress,bairro,num):
    config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'church',
    'raise_on_warnings':True
    }
    try:
        cnx = mysql.connector.connect(**config)
        my_data = cnx.cursor()
        sql = "INSERT INTO usuarios (nome,tel,endereco,bairro,numero) VALUES(%s,%s,%s,%s,%s)"
        val = (nome,tel,adress,bairro,num)
        my_data.execute(sql,val)
        cnx.commit()
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print('Algo esta errado com o nome de usuario e senha')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("database não existe")
        else:
            print(err)
    else:
        print(my_data.rowcount, "record inserted.")
        cnx.close()
   

    
insert_user(nome_usr,tel_usr,adress_usr,bairro_usr,num_usr)

