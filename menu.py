#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from colorama import init, Fore, Style                  # colorir terminal 
init(autoreset=True)                                    # inicializa o colorama e evita que ele continue após o print


#===================================================================================================================
#                                                BANNERS/TITULOS ESTILIZADOS
#===================================================================================================================

banner_inicio = f"""
{Fore.CYAN}{Style.BRIGHT}
██╗      █████╗ ██████╗    ██████╗ ██╗   ██╗
██║     ██╔══██╗██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║     ███████║██║  ██║   ██████╔╝ ╚████╔╝ 
██║     ██╔══██║██║  ██║   ██╔═══╝   ╚██╔╝  
███████╗██║  ██║██████╔╝██╗██║        ██║   
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝        ╚═╝   
{Fore.GREEN}{Style.BRIGHT}
 █▓▒▒░░░ SISTEMA DE VOTAÇÃO DIGITAL ░░░▒▒▓█
"""

#===================================================================================================================
#                                        MENUS DO MODULO DE GERENCIAMENTO
#===================================================================================================================

ger_menu = f"""
{Fore.CYAN}{Style.BRIGHT}
█▀▀ █▀▀ █▀█ █▀▀ █▄░█ █▀▀ █ ▄▀█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀█
█▄█ ██▄ █▀▄ ██▄ █░▀█ █▄▄ █ █▀█ █░▀░█ ██▄ █░▀█ ░█░ █▄█

[1]  CADASTRAR NOVO ELEITOR
[2]  ELEITORES
"""

ger_menu_eleitores = """
[1]  BUSCAR ELEITORES POR CPF/TÍTULO
[2]  LISTAR TODOS OS ELEITORES
"""

ger_menu_eleitores_opcao = """
[1]  EDITAR ELEITOR
[2]  REMOVER ELEITOR
"""

#===================================================================================================================
#                                        MENUS DO MODULO DE VOTAÇÃO
#===================================================================================================================

vot_menu = f"""
{Fore.CYAN}{Style.BRIGHT}
█░█ █▀█ ▀█▀ ▄▀█ █▀▀ ▄▀█ █▀█
▀▄▀ █▄█ ░█░ █▀█ █▄▄ █▀█ █▄█

[1]  ABRIR SISTEMA DE VOTAÇÃO
[2]  AUDITORIA DO SISTEMA DE VOTAÇÃO
[3]  RESULTADO DA VOTAÇÃO
"""
vot_menu_votacao = """
[1]  VOTAR
[2]  ENCERRAR SISTEMA DE VOTAÇÃO
"""

vot_menu_auditoria = """
[1]  EXIBIR LOGS DE OCORRÊNCIAS
[2]  EXIBIR PROTOCOLOS DA VOTAÇÃO
"""

vot_menu_resultado = """
[1]  BOLETIM DE URNA
[2]  ESTATÍSTICA DE COMPARECIMENTO
[3]  VOTOS POR PARTIDO
[4]  VALIDAÇÃO DA INTEGRIDADE DOS VOTOS
"""

print(vot_menu)