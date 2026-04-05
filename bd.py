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
    database = "LAD_Py"
)

if conexao.is_connected():
    msg.sucesso("Banco conectado com sucesso!")

cursor = conexao.cursor()

#===================================================================================================================
#                                         CRUD - CREATE, READ, UPDATE E DELETE
#===================================================================================================================

#================================
#          1. CREATE
#================================


#================================
#          2. READ
#================================

def listar_candidatos():
    cursor.execute("SELECT NumeroCandidato, NomeCandidato, PartidoCandidato FROM Candidatos ORDER BY NomeCandidato")
    candidatos = cursor.fetchall()
    
    if not candidatos:
        msg.alerta("Nenhum candidato cadastrado.")
        return
    
    print("\n")
    
    for candidato in candidatos:
        numero, nome, partido = candidato
        print(f"[{numero}] {nome} | {partido}")
    
    print("\n")
    

#================================
#          3. UPDATE
#================================


#================================
#          4. DELETE
#================================



listar_candidatos()