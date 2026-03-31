#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

import mysql.connector                                  # banco de dados
import msg                                              # documento msg.py com as mensagens de alerta

#===================================================================================================================
#                                          CONEXAO COM BANCO DE DADOS
#===================================================================================================================

conexao = mysql.connector.connect (
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1234",
    database = "bd_ladpy"
)

if conexao.is_connected():
    msg.sucesso("Banco conectado com sucesso!")
