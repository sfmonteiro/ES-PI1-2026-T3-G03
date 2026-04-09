# =====================================================================
#                           BIBLIOTECAS
# =====================================================================

import mysql.connector
from mysql.connector import Error, IntegrityError
from funcoes import msg
from dotenv import load_dotenv
import os
from funcoes import cor
from funcoes.mod_validacao import validar_titulo
from funcoes.mod_validacao import validar_cpf
from funcoes.modulo_criptografia import cifrar
from funcoes.modulo_criptografia import decifrar
from funcoes.mod_cacessoprotocolo import gerar_chave_acesso
from mysql.connector import IntegrityError, Error

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

        if conexao.is_connected():
            msg.sucesso("Banco conectado com sucesso!")

        return conexao

    except Error as erro:
        msg.alerta(f"Erro ao conectar: {erro}")
        return None


# =====================================================================
#                          CRUD - READ
# =====================================================================

def cadastrar_eleitor(nome, titulo, cpf, is_mesario):
    """
    Cadastra um eleitor, garantindo que a chave de acesso seja única no banco.

    Args:
        nome (str): Nome completo do eleitor.
        titulo (str): Título de eleitor (12 dígitos).
        cpf (str): CPF do eleitor (11 dígitos).
        is_mesario (bool): Indica se o eleitor atuará como mesário.

    Returns:
        bool: True para sucesso, False se houver erro de validação ou duplicidade de documentos.
    """
    # validação Matemática
    if not validar_cpf(cpf) or not validar_titulo(titulo):
        msg.erro("Documentos matematicamente inválidos!")
        return False

    conexao = conectar()
    if not conexao:
        return False

    tentando_cadastrar = True
    
    while tentando_cadastrar:
        # geração de nova chave a cada tentativa, para evitar colisões
        chave_bruta = gerar_chave_acesso(nome)

        # criptografia
        cpf_cifrado = cifrar(cpf) 
        chave_cifrada = cifrar(chave_bruta)
        titulo_cifrado = cifrar(titulo)

        try:
            cursor = conexao.cursor()
            query = """
            INSERT INTO eleitores 
            (nome, titulo_eleitor, cpf, chave_acesso, is_mesario, status_voto) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (nome, titulo_cifrado, cpf_cifrado, chave_cifrada, is_mesario, False)

            cursor.execute(query, valores)
            conexao.commit()

            # Se chegou aqui funcionou e a chave é única, então informa o usuário e sai do loop
            msg.sucesso(f"Eleitor cadastrado! CHAVE DE ACESSO: {chave_bruta}")
            tentando_cadastrar = False # sai do loop
            return True

        except IntegrityError as err:
            # verifica se o erro foi especificamente na chave_acesso (duplicidade)
            erro_msg = str(err)
            if "chave_acesso" in erro_msg:
                # Log interno: avisa que houve colisão de chave e tentará gerar outra
                print("Aviso: Chave duplicada gerada. Tentando nova combinação...")
                continue # volta para o início e gera nova chave
            else:
                # se o erro for CPF ou Título, para o processo
                msg.erro("Erro: CPF ou Título já cadastrado no sistema.")
                tentando_cadastrar = False
                return False
        
        except Error as e:
            msg.erro(f"Erro inesperado no banco: {e}")
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()

    if conexao.is_connected():
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
        SELECT *
        FROM eleitores
        """

        cursor.execute(query)
        eleitores = cursor.fetchall()
        return eleitores

    except Error as erro:
        msg.erro(f"Erro ao listar eleitores: {erro}")

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