import random
import string

from funcoes.mod_autenteleitor import autenticar_eleitor


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


def encerrar_votacao(titulo, primeiros_cpf, chave, conexao):
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
    # AUTENTICAÇÃO
    # ==========================
    
    resultado = autenticar_eleitor(titulo, primeiros_cpf, chave, conexao)
    
    if not resultado["sucesso"] or not resultado.get("is_mesario"):
        print("Falha na autenticação ou usuário não é mesário.")
        return False
    
    print("Mesário autenticado.")

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