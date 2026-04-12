# =====================================================================
#                           BIBLIOTECAS
# =====================================================================

import mysql.connector
from mysql.connector import Error, IntegrityError
from funcoes import mod_ger, msg
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

# =====================================================================
#                           1. CREATE
# =====================================================================

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
#                            2. READ
# =====================================================================

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

# =====================================================================
#                            3. UPDATE
# =====================================================================

def editar_eleitor(valor_busca, novos_dados):
    """
    Edita os dados de um eleitor no banco de dados usando CPF ou título de eleitor
    como critério de busca.

    A função identifica o tipo pela quantidade de dígitos informado:
    11 dígitos para CPF e 12 dígitos para título de eleitor.
    Se o nome for alterado, gera uma nova chave de acesso.

    Args:
        valor_busca (str): CPF ou título de eleitor usado para localizar o eleitor.
        novos_dados (dict): Dicionário com os campos permitidos para atualização.
        Campos permitidos: nome, chave_acesso, is_mesario.

    Returns:
        bool: True se a atualização ocorrer com sucesso, False caso contrário.
    """
    conexao = conectar()

    if not conexao:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        # Remove espaços, pontos e traços (verifica apenas dígitos)
        valor_limpo = "".join(char for char in str(valor_busca) if char.isdigit())

        if len(valor_limpo) == 11:
            campo_busca = "cpf"
        elif len(valor_limpo) == 12:
            campo_busca = "titulo_eleitor"
        else:
            msg.erro("CPF ou título de eleitor inválido. Quantidade de dígitos incorreta.")
            return False

        # Verifica se o eleitor existe
        query_busca = f"""
        SELECT nome
        FROM eleitores
        WHERE {campo_busca} = %s
        """
        cursor.execute(query_busca, (valor_limpo,))
        eleitor = cursor.fetchone()

        if not eleitor:
            msg.alerta("Nenhum eleitor encontrado com os dados informados.")
            return False

        nome_atual = eleitor[0]

        campos_permitidos = ["nome", "chave_acesso", "is_mesario"]

        # Se o nome mudou gera nova chave (AGUARDANDO FUNÇÃO DE GERER CHAVE)
        if "nome" in novos_dados and novos_dados["nome"] != nome_atual:
            novos_dados["chave_acesso"] = mod_ger.gerar_chave_acesso(novos_dados["nome"])

        campos_update = []
        valores = []

        for campo in campos_permitidos:
            if campo in novos_dados:
                campos_update.append(f"{campo} = %s")
                valores.append(novos_dados[campo])

        if not campos_update:
            msg.alerta("Nenhum campo válido foi informado para atualização.")
            return False

        query_update = f"""
        UPDATE eleitores
        SET {", ".join(campos_update)}
        WHERE {campo_busca} = %s
        """
        valores.append(valor_limpo)

        cursor.execute(query_update, tuple(valores))
        conexao.commit()

        if cursor.rowcount > 0:
            msg.sucesso("Eleitor atualizado com sucesso!")
            return True

        msg.alerta("Nenhuma alteração foi aplicada.")
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
#                            4. DELETE
# =====================================================================

def remover_eleitor(valor_busca):
    """
    Remove um eleitor do banco de dados usando CPF ou título de eleitor
    como critério de busca.

    A função identifica o tipo pela quantidade de dígitos informado:
    11 dígitos para CPF e 12 dígitos para título de eleitor.
    Se o nome for alterado, gera uma nova chave de acesso.

    Args:
        valor_busca (str): CPF ou título de eleitor usado para localizar o eleitor.

    Returns:
        bool: True se a remoção for realizada com sucesso, False caso contrário.
    """
    conexao = conectar()

    if not conexao:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        # Remove qualquer coisa que não seja número
        valor_limpo = "".join(char for char in str(valor_busca) if char.isdigit())

        # Identifica se é CPF ou título
        if len(valor_limpo) == 11:
            campo_busca = "cpf"
        elif len(valor_limpo) == 12:
            campo_busca = "titulo_eleitor"
        else:
            msg.erro("CPF ou título de eleitor inválido. Quantidade de dígitos incorreta.")
            return False

        # Executa a remoção
        query = f"""
        DELETE FROM eleitores
        WHERE {campo_busca} = %s
        """

        cursor.execute(query, (valor_limpo,))
        conexao.commit()

        if cursor.rowcount > 0:
            msg.sucesso("Eleitor removido com sucesso!")
            return True

        msg.alerta("Nenhum eleitor encontrado com os dados informados.")
        return False

    except Error as erro:
        msg.erro(f"Erro no banco: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()