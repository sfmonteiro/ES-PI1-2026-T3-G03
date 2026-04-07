import random
import string

def gerar_chave_acesso(nome_completo):
    """
    Gera uma chave de acesso baseada no nome do eleitor e dígitos aleatórios.
    
    Padrão: 2 primeiras letras do primeiro nome + 1ª letra do segundo nome 
    + 4 dígitos aleatórios. Ex: André Silva -> ANS4821.

    Args:
        nome_completo (str): O nome completo do eleitor.

    Returns:
        str: A chave de acesso gerada com 7 caracteres.
    """
    # Transforma o nome para maiúsculas e divide em partes
    partes_nome = nome_completo.upper().split()
    
    # Pega as duas primeiras letras do primeiro nome
    prefixo_primeiro = partes_nome[0][:2]
    
    # pega a primeira letra do segundo nome (se existir)
    # Caso o usuário só tenha um nome:
    if len(partes_nome) > 1:
        letra_segundo = partes_nome[1][0]
    else:
        letra_segundo = "X" #caso não haja sobrenome
        
    # gera 4 dígitos aleatórios
    digitos = str(random.randint(1000, 9999))
    
    # monta a chave final
    chave = prefixo_primeiro + letra_segundo + digitos
    return chave


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

if __name__ == "__main__":
    print(f"Chave: {gerar_chave_acesso('André Silva')}")
    print(f"Protocolo: {gerar_protocolo(99)}")