import random
import string
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
    Chama a função log_protocolos para gerar o arquivo txt e registrar os protocolos.

    Args:
        id_eleitor (int): id do eleitor identificado no login
        numero_candidato (int): O número do candidato escolhido pelo eleitor.

    Returns:
        Número de protocolo.
    """
        
    candidato = bd.listar_candidatos_numero(numero_candidato)

    if candidato:
        print(f"Candidato: {candidato['nome_candidato']} | Partido: {candidato['partido_candidato']}")
        id_candidato_db = candidato['id_candidato']
    else:
        msg.alerta("Candidato inexistente! Seu voto será computado como NULO.")
        id_candidato_db = None
    
    confirma = input(f"Confirma o voto no número {numero_candidato}? (S/N): ").upper()

    if confirma != 'S':
        msg.alerta("Voto cancelado. Retornando à inserção de número.")
        return "REPETIR"

    protocolo = gerar_protocolo(numero_candidato)
    protocolo_cifra = cripto.cifrar(protocolo)

    bd.insert_voto(id_candidato_db, protocolo_cifra)
    bd.editar_status_voto(id_eleitor)

    logs.log_protocolos(protocolo)

    return protocolo

    
def autenticar_eleitor(titulo, primeiros_cpf, chave_acesso_input):
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

def abrir_votacao(titulo, primeiros_cpf, chave):
    resultado = autenticar_eleitor(titulo, primeiros_cpf, chave)

    if not resultado['sucesso']:
        msg.erro(resultado['mensagem'])
        return False
    if not resultado['is_mesario']:
        msg.erro("Apenas mesários podem abrir a votação.")
        return False
    
    if not bd.zerezima_bd():
        return False
    votos = bd.listar_votos()
    if votos is False:
        return False
    
    return True


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
    
    resultado = autenticar_eleitor(titulo, primeiros_cpf, chave)
    
    if not resultado["sucesso"] or not resultado.get("is_mesario"):
        print("Falha na autenticação ou usuário não é mesário.")
        return False

    confirma = input("Deseja realmente encerrar a votação? (Sim/Não): ").strip().lower()
    if confirma != "sim":
        return False

    # Dupla confirmação da chave 
    chave_conf = input("Confirme sua chave para fechar a urna: ").strip()
    if chave_conf != chave:
        print("Chave incorreta para encerramento.")
        return False

    print("\nVotação encerrada com sucesso.") 
    return True