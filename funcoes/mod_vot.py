import random
import string
from funcoes import bd
from funcoes import cripto
from funcoes import logs
from funcoes import msg


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
    protocolo = gerar_protocolo(numero_candidato)
    protocolo_cifra = cripto.cifrar(protocolo)
    candidato = bd.listar_candidatos_numero(numero_candidato)
    if candidato == None:
        msg.erro("Esse candidato não existe.")
        return None
    bd.insert_voto(candidato['id_candidato'], protocolo_cifra)
    bd.editar_status_voto(id_eleitor)
    logs.log_protocolos(protocolo)
    return protocolo


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

    print("\nAutenticação do mesário")

    # ==========================
    # AUTENTICAÇÃO (STUB)
    # ==========================
    # Ainda não existe autenticar_eleitor(),
    # Simula que teve autenticação:

    autenticado = True
    # qndo autenticar_eleitor() pronto:
    # trocar autenticado = True p/ autenticado = autenticar_eleitor(titulo, primeiros_cpf, chave)

    if not autenticado:
        print("Falha na autenticação.")
        return False

    print("Mesário autenticado.")

    # ==========================
    # DUPLA CONFIRMAÇÃO DA CHAVE
    # ==========================
    print("\nConfirmação de segurança")

    chave_conf_1 = input("Digite a chave: ").strip()
    chave_conf_2 = input("Confirme a chave: ").strip()

    if chave_conf_1 != chave or chave_conf_2 != chave:
        print("Chaves não conferem.")
        return False

    print("Chave confirmada com sucesso.")

    # ==========================
    # ENCERRAMENTO
    # ==========================
    print("\nVotação encerrada com sucesso.")
    return True