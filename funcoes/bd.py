# =====================================================================
#                           BIBLIOTECAS
# =====================================================================

import mysql.connector
from mysql.connector import Error, IntegrityError
from funcoes import msg
from dotenv import load_dotenv
import os
from funcoes import cor

load_dotenv()

# =====================================================================
#                      FUNÇÃO DE CONEXÃO
# =====================================================================

def conectar():
    """
    Tenta realizar a conexão com o banco de dados MySQL usando variáveis de ambiente.

    Args:
        Nenhum.

    Returns:
        conexao (mysql.connector.connection): Objeto de conexão ativo com o banco de dados.
        None: Caso a conexão falhe.
    """
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        return conexao

    except Error as erro:
        msg.alerta(f"Erro ao conectar: {erro}")
        return None

def listar_chaves_existente(chave_acesso):
    """
    Lista todas as chaves de acesso dos eleitores cadastrados no banco de dados.

    Args:
        chave_acesso (str): A chave de acesso a ser pesquisada.

    Returns:
        list: Lista de tuplas com os dados dos eleitores que possuem a chave de acesso especificada.
        None: Se houver algum erro na consulta.
    """
    conexao = conectar()
    if not conexao:
        return True

    try:
        cursor = conexao.cursor()

        query = """
        SELECT *
        FROM eleitores
        WHERE chave_acesso = %s
        """
        cursor.execute(query, (chave_acesso,))
        eleitores = cursor.fetchall()
        return eleitores

    except Error as erro:
        msg.alerta(f"Erro ao listar chaves existentes: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()


# =====================================================================
#                          CRUD - READ
# =====================================================================

def listar_candidatos():
    """
    Lista todos os candidatos cadastrados no banco de dados,
    exibindo número, nome e partido em ordem alfabética.

    Args:
        Nenhum.

    Returns:
        None
    """
    conexao = conectar()
    if not conexao:
        return
    
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

        print(cor.magenta("\n█▓▒▒░░░    LISTAGEM DE CANDIDATOS    ░░░▒▒▓█\n"))

        for candidato in candidatos:
            numero, nome, partido = candidato
            print(f"[{numero}] {nome} | {partido}")

    except Error as erro:
        msg.alerta(f"Erro ao listar candidatos: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
        
def listar_eleitores():
    """
    Lista todos os eleitores cadastrados no banco de dados.

    Args:
        Nenhum.

    Returns:
        list: Lista de tuplas com os dados de todos os eleitores.
        None: Se houver algum erro na consulta.
    """
    conexao = conectar()
    if not conexao:
        return
    
    try:
        cursor = conexao.cursor()

        query = """
        SELECT id_eleitor, nome, titulo_eleitor, cpf, is_mesario
        FROM eleitores
        """

        cursor.execute(query)
        eleitores = cursor.fetchall()

        for eleitor in eleitores:
            id_eleitor, nome, titulo, cpf, is_mesario= eleitor
            mesario = "SIM" if is_mesario == 1 else "NÃO"
            print(f"{cor.ciano("[" + str(id_eleitor) + "]")} {nome} | Título: {titulo} | CPF: {cpf} | Mesário: {mesario}")
        return eleitores

    except Error as erro:
        msg.erro(f"Erro ao listar eleitores: {erro}")

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def cadastrar_eleitor(nome, titulo, cpf, chave_acesso, is_mesario):
    """
    Cadastra um eleitor no banco de dados com base nas variáveis inseridas.

    Args:
        nome (str): Nome completo do eleitor.
        titulo (int): Título de eleitor.
        cpf (int): CPF do eleitor.
        is_mesario (bool): Indica se o eleitor é mesário.
        chave_acesso (str): Chave de acesso gerada para o eleitor.

    Returns:
        True: Quando o eleitor é cadastrado com sucesso.
        False: Quando há CPF ou título já cadastrado, ou quando há erro de conexão com o banco.
    """
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

        valores = (nome, titulo, cpf, chave_acesso, is_mesario, False)

        cursor.execute(query, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            return True
        else:
            return False

    except IntegrityError:
        msg.erro("CPF ou título de eleitor já cadastrado.")
        return False

    except Error as erro:
        msg.erro(f"Erro no banco: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

# =====================================================================
#                          EXECUÇÃO
# =====================================================================

if __name__ == "__main__":
    listar_eleitores()
    cadastrar_eleitor("gabi", "6543218", "44157014765", False, False)