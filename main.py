#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================
import menu
import msg
import cor
from colorama import init, Fore, Style                  # colorir terminal 
init(autoreset=True)                                    # inicializa o colorama e evita que ele continue após o print

#===================================================================================================================
#                                                 INÍCIO
#===================================================================================================================

print(menu.banner_inicio)

#=================== MENU MODULO INICIAL ====================
op_mod = -1

while (op_mod != 0):
    print(menu.modulo)
    op_mod = menu.selecionar_opcao()

    match op_mod:
        
        #=================== MENU MODULO GERENCIAMENTO ====================
        case 1:

            op_ger = -1

            while (op_ger != 0):
                print(menu.ger_menu)
                op_ger = menu.selecionar_opcao()

                match op_ger:

                    #=================== CADASTRAR ELEITOR ====================
                    case 1: 
                        print(cor.ciano("\n█▓▒▒░░░ CADASTRO DO ELEITOR ░░░▒▒▓█"))
                        msg.alerta("[Cadastro do eleitor]")

                    #=================== ELEITORES (GERENCIAR) ====================
                    case 2:
                        op_ger_eleitores = -1

                        while (op_ger_eleitores != 0):
                            print(cor.ciano("\n█▓▒▒░░░      ELEITORES       ░░░▒▒▓█"))
                            print(menu.ger_menu_eleitores)
                            op_ger_eleitores = menu.selecionar_opcao()

                            match op_ger_eleitores:
                                
                                #=================== MENU BUSCAR ELEITORES POR CPF OU TITULO ====================
                                case 1:
                                    msg.alerta("[Digitar CPF ou Título]")

                                    op_editar_eleitor = -1

                                    while (op_editar_eleitor != 0):
                                        print(menu.ger_menu_eleitores_opcao)
                                        op_editar_eleitor = menu.selecionar_opcao()

                                        match op_editar_eleitor:

                                            #=================== MENU EDITAR ELEITOR ====================
                                            case 1:
                                                msg.alerta("[Editar campos, talvez mais um while para cada opção]")
                                            case 2:
                                                msg.alerta("[Remover eleitor]")
                                            case 0:
                                                msg.alerta("Voltando para o menu anterior...")
                                            case _:
                                                msg.erro("Opção inválida.")
                                
                                #=================== MENU LISTAR TODOS OS ELEITORES ====================
                                case 2:
                                    msg.alerta("[Listar todos os eleitores cadastrados]")

                                case 0:
                                    msg.alerta("Voltando ao módulo de Gerenciamento...")

                                case _:
                                    msg.erro("Opção inválida.")

                    case 0:
                        msg.alerta("Voltando à seleção dos módulos...")
                    case _:
                        msg.erro("Opção inválida.")

        #=================== MENU MODULO VOTAÇÃO ====================
        case 2:
            msg.alerta("[modulo votação]")
        
        case 0:
            msg.alerta("Encerrando o programa...")
            break

        case _:
            msg.erro("Opção inválida.")

        
                    