import random
import string
import time

from mysql.connector import Error

from funcoes import cor
from . import bd
from . import cripto
from . import logs
from . import msg 
from .cripto import decifrar 

def gerar_protocolo(numero_candidato):
    """
    Gera um protocolo de votação exclusivo após a confirmação do voto.
    
    Padrão: Prefixo 'V' + 2 letras aleatórias + Ano (26) + 
    Número do Candidato (2 dígitos) + 5 dígitos aleatórios.

    Args:
        numero_candidato (int): O número do candidato escolhido pelo eleitor.

    Returns:
        str: O protocolo de votação gerado com 12 caracteres.
    """
    # prefixo fixo 'V'
    prefixo = "V"
    
    # gerar 2 letras aleatórias maiúsculas
    letras_aleatorias = "".join(random.choices(string.ascii_uppercase, k=2))
    
    # ano fixo do projeto
    ano = "26"
    
    # garantir que o número do candidato tenha 2 dígitos (ex: 7 vira 07)
    cand_formatado = str(numero_candidato).zfill(2)
    
    # gerar 5 dígitos aleatórios
    final_aleatorio = "".join(random.choices(string.digits, k=5))
    
    # montar o protocolo final
    protocolo = prefixo + letras_aleatorias + ano + cand_formatado + final_aleatorio
    return protocolo

def registrar_voto(id_eleitor, numero_candidato):
    """
    Chama a função de gerar_protocolo e adiciona a cifra no protocolo gerado.
    Chama a função listar_candidatos pelo número para encontrar o candidato que o eleitor escolheu.
    Chama a função insert_voto para salvar no banco de dados as informações.
    Chama a função editar_status_voto para atualizar o atributo status_voto no bd.

    Args:
        id_eleitor (int): id do eleitor identificado no login
        numero_candidato (int): O número do candidato escolhido pelo eleitor.

    Returns:
        Número de protocolo.
    """
        
    candidato = bd.listar_candidatos_numero(numero_candidato)


    if candidato:
        print(f"\nCandidato: {candidato['nome_candidato']} | Partido: {candidato['partido_candidato']}")
        id_candidato_db = candidato['id_candidato']
    else:
        msg.alerta("Candidato inexistente! Seu voto será computado como NULO.")
        id_candidato_db = None
    
    confirma = input(f"Confirma o voto no número {numero_candidato}? (S/N): ").upper()

    if confirma != 'S':
        msg.alerta("Voto cancelado. Retornando à inserção de número...")
        time.sleep(1.5)
        return "REPETIR"

    protocolo = gerar_protocolo(numero_candidato)
    protocolo_cifra = cripto.cifrar(protocolo)

    bd.insert_voto(id_candidato_db, protocolo_cifra)
    bd.editar_status_voto(id_eleitor)

    return protocolo

    
def autenticar_eleitor(titulo, primeiros_cpf, chave_acesso_input, arquivo_log):
    """
    Valida as credenciais do eleitor e verifica se ele já realizou o voto.

    A função consulta o banco pelo título, decifra o CPF e a chave para 
    conferência e checa o status do voto. Não altera dados no BD.

    Args:
        titulo (str): O número do título de eleitor informado.
        primeiros_cpf (str): Os 4 primeiros dígitos do CPF para validação.
        chave_acesso_input (str): A chave de acesso fornecida pelo eleitor.
        conexao (mysql.connector.connection): Conexão ativa com o banco de dados.

    Returns:
        dict: Um dicionário com 'sucesso' (bool) e 'mensagem' (str). 
              Se sucesso, inclui também o 'id_eleitor'.
    """
    conexao = bd.conectar()
    cursor = None
    try:
        cursor = conexao.cursor(dictionary=True)
        
        # consulta a base de dados pelo título
        query = "SELECT id_eleitor, cpf, chave_acesso, status_voto, is_mesario FROM eleitores WHERE titulo_eleitor = %s"
        titulo_cripto = cripto.cifrar(titulo)
        cursor.execute(query, (titulo_cripto,))
        eleitor = cursor.fetchone()

        if not eleitor:
            return {"sucesso": False, "mensagem": "Eleitor não encontrado."}

        # decifrar os dados para comparação
        cpf_real = cripto.decifrar(eleitor['cpf'], "cpf")
        chave_real = cripto.decifrar(eleitor['chave_acesso'], "chave")

        # validação das credenciais
        # compara os 4 primeiros dígitos do CPF e a chave de acesso
        if cpf_real[:4] != primeiros_cpf or chave_real != chave_acesso_input:
            return {"sucesso": False, "mensagem": "Dados de identificação inválidos."}
        
        # verifica se já votou
        if eleitor['status_voto']:
            logs.voto_duplo(arquivo_log)
            return {"sucesso": False, "mensagem": "ALERTA: Este eleitor já realizou o voto."}

        # Se passou por tudo, identificação bem-sucedida
        return {
            "sucesso": True, 
            "mensagem": "Eleitor autenticado com sucesso.",
            "is_mesario": eleitor['is_mesario'],
            "id_eleitor": eleitor['id_eleitor']
        }

    except Exception as e:
        return {"sucesso": False, "mensagem": f"Erro na autenticação: {e}"}
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def autenticar_mesario(titulo, primeiros_cpf, chave_acesso_input):
    """
    Valida as credenciais do mesário e verifica se ele está autorizado.

    A função consulta o banco pelo título, decifra o CPF e a chave para 
    conferência e checa o status do mesário. Não altera dados no BD.

    Args:
        titulo (str): O número do título de eleitor informado.
        primeiros_cpf (str): Os 4 primeiros dígitos do CPF para validação.
        chave_acesso_input (str): A chave de acesso fornecida pelo eleitor.
        conexao (mysql.connector.connection): Conexão ativa com o banco de dados.

    Returns:
        dict: Um dicionário com 'sucesso' (bool) e 'mensagem' (str). 
              Se sucesso, inclui também o 'id_eleitor'.
    """
    conexao = bd.conectar()
    cursor = None
    try:
        cursor = conexao.cursor(dictionary=True)
        
        # consulta a base de dados pelo título
        query = "SELECT id_eleitor, cpf, chave_acesso, status_voto, is_mesario FROM eleitores WHERE titulo_eleitor = %s"
        titulo_cripto = cripto.cifrar(titulo)
        cursor.execute(query, (titulo_cripto,))
        eleitor = cursor.fetchone()

        if not eleitor:
            return {"sucesso": False, "mensagem": "Mesário não encontrado."}

        # decifrar os dados para comparação
        cpf_real = cripto.decifrar(eleitor['cpf'], "cpf")
        chave_real = cripto.decifrar(eleitor['chave_acesso'], "chave")

        # validação das credenciais
        # compara os 4 primeiros dígitos do CPF e a chave de acesso
        if cpf_real[:4] != primeiros_cpf or chave_real != chave_acesso_input:
            return {"sucesso": False, "mensagem": "Dados de identificação inválidos."}
        


        # Se passou por tudo, identificação bem-sucedida
        return {
            "sucesso": True, 
            "mensagem": "Mesário autenticado com sucesso.",
            "is_mesario": eleitor['is_mesario'],
            "id_eleitor": eleitor['id_eleitor']
        }

    except Exception as e:
        return {"sucesso": False, "mensagem": f"Erro na autenticação: {e}"}
    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def abrir_votacao(titulo, primeiros_cpf, chave, arquivo_log):
    bd.zerezima_bd()
    resultado = autenticar_mesario(titulo, primeiros_cpf, chave)

    if not resultado['sucesso']:
        logs.acesso_negado(arquivo_log)
        msg.erro(resultado['mensagem'])
        time.sleep(1.5)
        return False
    if not resultado['is_mesario']:
        msg.alerta("Apenas mesários podem abrir a votação.")
        time.sleep(1.5)
        logs.acesso_negado(arquivo_log)
        return False
    

    if not bd.zerezima_bd():
        return False
    
    logs.zerezima(arquivo_log)
    
    return arquivo_log


def encerrar_votacao(titulo, primeiros_cpf, chave):
    """
    Encerra a votação com autenticação de um mesário
    e dupla confirmação da chave de acesso.

    Args:
        titulo (str): Título de eleitor do mesário.
        primeiros_cpf (str): Primeiros dígitos do CPF.
        chave (str): Chave de acesso do mesário.

    Returns:
        bool: True se a votação for encerrada com sucesso, False caso contrário.
    """

    # ==========================
    # AUTENTICAÇÃO
    # ==========================
    
    resultado = autenticar_mesario(titulo, primeiros_cpf, chave)
    
    if not resultado["sucesso"] or not resultado['is_mesario']:
        msg.erro("Falha na autenticação ou usuário não é mesário.")
        return False

    confirma = input("Deseja realmente encerrar a votação? (Sim/Não): ").strip().lower()
    if confirma != "sim":
        return False

    # Dupla confirmação da chave 
    chave_conf = input("Confirme sua chave para fechar a urna: ").strip()
    if chave_conf != chave:
        msg.erro("Chave incorreta para encerramento.")
        return False

    return True


def mostrar_protocolo(protocolo):
    """
    Exibe o protocolo formado em uma caixa no terminal.

    Args:
        protocolo (str): protocolo a ser exibido.

    Returns:
        str: o próprio protocolo.       
    """
    print(f"""

    {cor.azul("   Seu protocolo é:")}
{cor.ciano(f"""╔════════════════════════════╗
║        {protocolo}        ║
╚════════════════════════════╝""")}
 {cor.preto(">> Guarde-a com segurança <<")}
""")

def exibir_protocolos():
    """
    Busca os protocolos cifrados do banco de dados, decifra e exibe em ordem alfabética.

    Returns:
        bool: True se a listagem for exibida com sucesso, False em caso de erro.
    """
    conexao = bd.conectar()
    if not conexao:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        query = """
        SELECT protocolo
        FROM votos
        """
        cursor.execute(query)
        registros = cursor.fetchall()

        if not registros:
            msg.alerta("Nenhum protocolo cadastrado.")
            return None

        protocolos = []
        for (protocolo_cifrado,) in registros:
            protocolo_decifrado = decifrar(protocolo_cifrado, "protocolo")
            if protocolo_decifrado:
                protocolos.append(protocolo_decifrado)

        if not protocolos:
            msg.alerta("Erro ao buscar protocolos.")
            return None

        protocolos.sort()

        for indice, protocolo in enumerate(protocolos, start=1):
            print(f"{indice:03d}. {protocolo}")

        return True

    except Error as erro:
        msg.erro(f"Erro ao exibir protocolos: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def boletim_urna():
    """
    Exibe o boletim de urna com os votos consolidados por candidato.

    Args:
        Nenhum.

    Returns:
        bool: True se o boletim for exibido, False caso contrário.
    """
    resultados = bd.listar_resultados()

    if not resultados:
        msg.alerta("Nenhum resultado encontrado.")
        return False

    # print(cor.magenta("\n█▓▒▒░░░    BOLETIM DE URNA    ░░░▒▒▓█\n"))

    for candidato in resultados:
        print(
            f"[{candidato['numero_candidato']}] "
            f"{candidato['nome_candidato']} | "
            f"{candidato['partido_candidato']} | "
            f"Votos: {candidato['total_votos']}"
        )

    return True


def declarar_vencedor():
    """
    Declara o vencedor da votação ou informa empate entre candidatos.

    Args:
        Nenhum.

    Returns:
        bool: True se o resultado for exibido, False caso contrário.
    """
    resultados = bd.listar_resultados()

    if not resultados:
        msg.alerta("Nenhum resultado encontrado.")
        return False

    maior_votos = 0

    for candidato in resultados:
        if candidato['total_votos'] > maior_votos:
            maior_votos = candidato['total_votos']

    if maior_votos == 0:
        msg.alerta("Nenhum voto registrado. Não há vencedor.")
        return False

    empatados = []

    for candidato in resultados:
        if candidato['total_votos'] == maior_votos:
            empatados.append(candidato)

    if len(empatados) > 1:
        print(cor.magenta("\n█▓▒▒░░░    EMPATE NA VOTAÇÃO    ░░░▒▒▓█\n"))

        for candidato in empatados:
            print(
                f"[{candidato['numero_candidato']}] "
                f"{candidato['nome_candidato']} | "
                f"{candidato['partido_candidato']} | "
                f"Votos: {candidato['total_votos']}"
            )

        return True

    vencedor = empatados[0]

    print(cor.magenta("\n█▓▒▒░░░    VENCEDOR DA VOTAÇÃO    ░░░▒▒▓█\n"))

    print(
        f"{vencedor['nome_candidato']} | "
        f"Número: {vencedor['numero_candidato']} | "
        f"Partido: {vencedor['partido_candidato']} | "
        f"Votos: {vencedor['total_votos']}"
    )

    return True

def calcular_votos_por_partido():
    """
    Calcula a quantidade total de votos recebidos por cada partido.

    Realiza uma consulta SQL que cruza as tabelas de votos e candidatos,
    agrupando os resultados e ordenando do partido mais votado para o menos votado.

    Returns:
        list: Uma lista de dicionários, onde cada dicionário contém as chaves 
        'partido' e 'total_votos'. Retorna lista vazia se houver erro.
    """

    conexao = bd.conectar()
    
    try:
        # dictionary=True facilita a leitura dos dados no Python depois
        cursor = conexao.cursor(dictionary=True)
        
        query = """
            SELECT c.partido, COUNT(v.id_voto) AS total_votos
            FROM votos v
            JOIN candidatos c ON v.id_candidato = c.id_candidato
            GROUP BY c.partido
            ORDER BY total_votos DESC
        """
        
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        return resultados

    except Exception as e:
        msg.erro(f"Erro ao calcular votos por partido: {e}")
        return []
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conexao' in locals() and conexao and conexao.is_connected():
            conexao.close()

def calcular_estatisticas_comparecimento():
    """
    Calcula as estatísticas de comparecimento dos eleitores na urna.

    Consulta a tabela de eleitores para contabilizar o total de cadastrados
    e quantos destes possuem o status_voto como verdadeiro.

    Returns:
        dict: Dicionário contendo 'total', 'presentes', 'ausentes' e 'percentual'.
              Retorna None em caso de erro.
    """

    conexao = bd.conectar()
    
    try:
        cursor = conexao.cursor(dictionary=True)
        
        query = """
            SELECT 
                COUNT(*) AS total_eleitores,
                SUM(CASE WHEN status_voto = 1 THEN 1 ELSE 0 END) AS presentes
            FROM eleitores
        """
        
        cursor.execute(query)
        resultado = cursor.fetchone()

        # Tratamento caso o banco retorne nulo para total ou presentes
        total = resultado['total_eleitores'] if resultado['total_eleitores'] else 0
        presentes = int(resultado['presentes']) if resultado['presentes'] else 0
        ausentes = total - presentes
        
        # Evita o erro de "divisão por zero" se não houver ninguém cadastrado
        percentual = (presentes / total * 100) if total > 0 else 0.0

        return {
            "total": total,
            "presentes": presentes,
            "ausentes": ausentes,
            "percentual": round(percentual, 2)
        }

    except Exception as e:
        print(f"Erro ao calcular estatísticas de comparecimento: {e}")
        return None
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()