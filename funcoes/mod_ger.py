#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import bd, mod_validacao
from funcoes import menu
from funcoes import cor
from funcoes import msg
import random

def validar_nome(nome):
        if nome == "" or len(nome.split()) < 2 or any(char.isdigit() for char in nome):
            return False
        else:
            return True
        
def input_voltar():

    opcao = input(cor.amarelo(f"\n>> Pressione {cor.vermelho("[0] para voltar ao menu")}{cor.amarelo(", ou ENTER para tentar novamente...  ")}")).strip()
    menu.limpar_terminal()
    menu.mostrar_ger_cad_eleitores()
    if opcao == "0":
        return True
    else:
        return False
    
#===================================================================================================================

def menu_cad_eleitor ():
    """
    Exibe um menu passo a passo para coletar os dados de cadastro de um eleitor.

    Args:
        Nenhum.

    Returns:
        dict: Dicionário com os dados coletados do eleitor, contendo as chaves:
            - "nome" (str): Nome completo do eleitor.
            - "titulo_eleitor" (str): Título de eleitor (apenas números).
            - "cpf" (str): CPF do eleitor (apenas números).
            - "chave_acesso" (str): Inicializada vazia, preenchida posteriormente.
            - "is_mesario" (bool): True se o eleitor é mesário, False caso contrário.
    """
    dict_cadastro = {
        "nome": "",
        "titulo_eleitor": "",
        "cpf": "",
        "is_mesario": ""
    }
    for i in range(4):
        
        print(cor.ciano(f"Passo {i+1} de 4..."))
        if i == 0:
            nome_errado = True
            while nome_errado:
                nome = input("Digite seu nome completo:  ")
                if validar_nome(nome):
                    dict_cadastro["nome"] = nome
                    nome_errado = False
                else:
                    menu.limpar_terminal()
                    msg.erro("Nome inválido. Digite seu nome e sobrenome.")
                    voltar = input_voltar()
                    if voltar:
                        return None

        elif i == 1:
            titulo_errado = True
            while titulo_errado:
                titulo = input("Digite seu título de eleitor (apenas números):  ").strip()
                if mod_validacao.validar_titulo(titulo):
                    dict_cadastro["titulo_eleitor"] = titulo
                    titulo_errado = False
                else:
                    menu.limpar_terminal()
                    msg.erro("Título de eleitor inválido. Digite um número válido.")
                    voltar = input_voltar()
                    if voltar:
                        return None

        elif i == 2:
            cpf_errado = True
            while cpf_errado:
                cpf = input("Digite seu CPF (apenas números):  ").strip()
                if mod_validacao.validar_cpf(cpf):
                    dict_cadastro["cpf"] = cpf
                    cpf_errado = False
                else:
                    menu.limpar_terminal()
                    msg.erro("CPF inválido. Digite um número válido.")
                    voltar = input_voltar()
                    if voltar:
                        return None

        elif i == 3:
            opcao_errada = True
            while opcao_errada:
                opcao = input(f"É mesário? {cor.verde("[1] SIM")} {cor.vermelho("[0] NÃO")} : ").strip()
                if opcao in ["0", "1"]:
                    opcao_errada = False
                else:
                    menu.limpar_terminal()
                    msg.erro(f"Opção inválida. Digite {cor.verde('[1] para SIM')} ou {cor.vermelho('[0] para NÃO')}.")
                    voltar = input_voltar()
                    if voltar:
                        return None

            dict_cadastro["is_mesario"] = True if opcao == "1" else False
    
    menu.limpar_terminal()

    return dict_cadastro
        
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


def mostrar_chave_acesso(chave):
    """
    Exibe a chave de aceso formada em uma caixa no terminal.

    Args:
        chave (str): chave a ser exibida.

    Returns:
        str: a própria chave de acesso.       
    """
    print(f"""

    {cor.azul("Sua chave de acesso é:")}
{cor.ciano(f"""╔════════════════════════════╗
║          {chave}           ║
╚════════════════════════════╝""")}
 {cor.preto(">> Guarde-a com segurança <<")}
""")

