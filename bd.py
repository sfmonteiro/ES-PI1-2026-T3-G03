# =====================================================================
#                           BIBLIOTECAS
# =====================================================================

<<<<<<< HEAD
import mysql.connector
from mysql.connector import Error, IntegrityError
import msg
from dotenv import load_dotenv
import os
=======
import mysql.connector                                  # banco de dados
import msg                                              # documento msg.py com as mensagens de alerta
import cor
>>>>>>> main

load_dotenv()

# =====================================================================
#                      FUNÇÃO DE CONEXÃO
# =====================================================================

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if conexao.is_connected():
            msg.sucesso("Banco conectado com sucesso!")

        return conexao

    except Error as erro:
        msg.alerta(f"Erro ao conectar: {erro}")
        return None


# =====================================================================
#                          CRUD - READ
# =====================================================================

def listar_candidatos():
<<<<<<< HEAD
    conexao = conectar()
=======
    """
    Lista todos os candidatos cadastrados no banco de dados.

    Args:
        Nenhum.

    Returns:
        None
    """
    cursor.execute("SELECT NumeroCandidato, NomeCandidato, PartidoCandidato FROM Candidatos ORDER BY NomeCandidato")
    candidatos = cursor.fetchall()
>>>>>>> main
    
    if not conexao:
        return
    
<<<<<<< HEAD
    try:
        cursor = conexao.cursor()

        query = """
        SELECT numero_candidato, nome_candidato, partido_candidato
        FROM candidatos
        ORDER BY nome_candidato
        """

        cursor.execute(query)
        candidatos = cursor.fetchall()

        if not candidatos:
            msg.alerta("Nenhum candidato cadastrado.")
            return

        print("\n")

        for numero, nome, partido in candidatos:
            print(f"[{numero}] {nome} | {partido}")

        print("\n")

    except Error as erro:
        msg.alerta(f"Erro ao listar candidatos: {erro}")

    finally:
        cursor.close()
        conexao.close()
        
def listar_eleitores():
    conexao = conectar()
    
    if not conexao:
        return
    
    try:
        cursor = conexao.cursor()

        query = """
        SELECT *
        FROM eleitores
        """

        cursor.execute(query)
        eleitores = cursor.fetchall()
        return eleitores

    except Error as erro:
        msg.alerta(f"Erro ao listar eleitores: {erro}")

    finally:
        cursor.close()
        conexao.close()

def cadastrar_eleitor(nome, titulo, cpf, is_mesario, chave_acesso):
    conexao = conectar()

    if not conexao:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        query = """
        INSERT INTO eleitores
        (nome, titulo_eleitor, cpf, chave_acesso, is_mesario, status_voto)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            titulo,
            cpf,              
            chave_acesso,     
            is_mesario,
            False
        )

        cursor.execute(query, valores)
        conexao.commit()

        msg.sucesso("Eleitor cadastrado com sucesso!")
        return True

    except IntegrityError:
        msg.alerta("CPF ou título de eleitor já cadastrado.")
        return False

    except Error as erro:
        msg.alerta(f"Erro no banco: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
=======
    print(cor.magenta("\n█▓▒▒░░░    LISTAGEM DE CANDIDATOS    ░░░▒▒▓█\n"))

    for candidato in candidatos:
        numero, nome, partido = candidato
        print(f"[{numero}] {nome} | {partido}")

>>>>>>> main
    

# =====================================================================
#                          EXECUÇÃO
# =====================================================================

if __name__ == "__main__":
    listar_eleitores()
    cadastrar_eleitor("gabi", "654321", "44157014768", False, False)