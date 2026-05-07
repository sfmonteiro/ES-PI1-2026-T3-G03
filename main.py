#===================================================================================================================
#                                                 BIBLIOTECAS
#===================================================================================================================

from funcoes import menu
from funcoes import mod_ger
from funcoes import msg
from funcoes import cor
from funcoes import logs
from funcoes import bd
from funcoes import mod_ger
from funcoes import cripto
from funcoes import mod_vot
import time
from getpass import getpass

#===================================================================================================================
#                                                     MAIN
#===================================================================================================================

#=================== INICIO DO SISTEMA ====================
menu.limpar_terminal()
menu.mostrar_inicio()
input(cor.amarelo(">> Pressione ENTER para iniciar o programa LAD.PY...  "))

#=================== MENU MODULO INICIAL ====================
op_mod = -1

while (op_mod != 0):
    menu.limpar_terminal()
    menu.mostrar_modulos()
  
    op_mod = menu.selecionar_opcao()

    match op_mod:
        
        #=================== MENU MODULO GERENCIAMENTO ====================
        case 1:

            op_ger = -1

            while (op_ger != 0):
                menu.limpar_terminal()
                menu.mostrar_ger()
                op_ger = menu.selecionar_opcao()

                match op_ger:

                    #=================== CADASTRAR ELEITOR ====================
                    case 1: 
                        menu.limpar_terminal()
                        menu.mostrar_ger_cad_eleitores()

                        dict_cadastro = mod_ger.menu_cad_eleitor()
                        if dict_cadastro is None:
                            msg.alerta("Voltando para o menu anterior...")
                            time.sleep(1.5)
                            continue

                        chave_gerada = mod_ger.gerar_chave_acesso(dict_cadastro['nome'])

                        eleitor = bd.cadastrar_eleitor(
                            dict_cadastro['nome'],
                            dict_cadastro['titulo_eleitor'],
                            dict_cadastro['cpf'],
                            dict_cadastro['is_mesario']
                            )
                        if eleitor:
                            msg.sucesso("Eleitor cadastrado com sucesso!")

                        input(cor.amarelo("\n\n>> Pressione ENTER para retornar ao menu anterior...  "))

                    #=================== ELEITORES (GERENCIAR) ====================
                    case 2:
                        op_ger_eleitores = -1

                        while (op_ger_eleitores != 0):
                            menu.limpar_terminal()
                            menu.mostrar_ger_eleitores()
                            op_ger_eleitores = menu.selecionar_opcao()

                            match op_ger_eleitores:
                                
                                #=================== MENU BUSCAR ELEITORES POR CPF OU TITULO ====================
                                case 1:
                                    menu.limpar_terminal()
                                    menu.mostrar_ger_eleitores_cadastrados()

                                    valor_busca = input("Digite CPF ou título do eleitor: ").strip()

                                    eleitor = bd.buscar_eleitor(valor_busca)

                                    if not eleitor:
                                        msg.alerta("Eleitor não encontrado.")
                                        input(cor.amarelo("\n>> Pressione ENTER para retornar ao menu anterior...  "))
                                        continue

                                    id_eleitor, nome, titulo, cpf, is_mesario = eleitor
                                    mesario = "SIM" if is_mesario else "NÃO"

                                    cpf_decifrado = cripto.decifrar(cpf, "cpf")
                                    titulo_decifrado = titulo

                                    menu.limpar_terminal()
                                    menu.mostrar_ger_eleitores_cadastrados()

                                    print(f"{cor.ciano(f'[{id_eleitor}]')} {nome} | Título: {titulo_decifrado} | CPF: {cpf_decifrado} | Mesário: {mesario}")

                                    print("\nDeseja editar este eleitor?")
                                    print(cor.verde("\n[1] SIM"))
                                    print(cor.vermelho("[2] NÃO\n"))

                                    confirmar = menu.selecionar_opcao()

                                    if confirmar != 1:
                                        msg.alerta("Operação cancelada.")
                                        input(cor.amarelo("\n>> Pressione ENTER para retornar ao menu...  "))
                                        continue

                                    op = -1

                                    while op != 0:
                                        menu.limpar_terminal()
                                        menu.mostrar_ger_eleitores_edit()
                                        op = menu.selecionar_opcao()

                                        match op:
                                            #=================== MENU EDITAR ELEITOR ====================
                                            case 1:
                                                menu.limpar_terminal()
                                                menu.mostrar_ger_cad_eleitores()

                                                novos_dados = {}
                                                
                                                nome_invalido = True
                                                while nome_invalido:
                                                    print(cor.ciano("Passo 1 de 2..."))
                                                    novo_nome = input("Digite seu novo nome (pressione ENTER p/ manter): ").strip()

                                                    if novo_nome == "":
                                                        break
                                                    if mod_ger.validar_nome(novo_nome):
                                                        novos_dados["nome"] = novo_nome
                                                        nome_invalido = False
                                                    else:
                                                        msg.erro("Nome inválido. Digite seu nome e sobrenome.")
                                                        input(cor.amarelo("\n>> Pressione ENTER para tentar novamente...  "))
                                                        menu.limpar_terminal()
                                                        menu.mostrar_ger_cad_eleitores()
                                                
                                                menu.limpar_terminal()
                                                menu.mostrar_ger_cad_eleitores()

                                                opcao_invalida = True
                                                while opcao_invalida:
                                                    print(cor.ciano("Passo 2 de 2..."))
                                                    print("Status de mesário:")
                                                    print(cor.verde("\n[1] É MESÁRIO"))
                                                    print(cor.vermelho("[2] NÃO É MESÁRIO"))
                                                    print(cor.ciano("[0] MANTER STATUS ATUAL\n"))

                                                    op_mesario = menu.selecionar_opcao()
                                                    menu.limpar_terminal()
                                                    menu.mostrar_ger_cad_eleitores()

                                                    if op_mesario in [0, 1, 2]:
                                                        opcao_invalida = False
                                                    else:
                                                        menu.limpar_terminal()
                                                        menu.mostrar_ger_cad_eleitores()
                                                        msg.erro("Opção inválida. Digite 1, 2 ou 0.")
                                                        input(cor.amarelo("\n>> Pressione ENTER para tentar novamente...  "))
                                                        menu.limpar_terminal()
                                                        menu.mostrar_ger_cad_eleitores()

                                                if op_mesario == 1:
                                                    novos_dados["is_mesario"] = True
                                                elif op_mesario == 2:
                                                    novos_dados["is_mesario"] = False

                                                if novos_dados:
                                                    bd.editar_eleitor(valor_busca, novos_dados)
                                                else:
                                                    msg.alerta("Nada para atualizar.")

                                                input(cor.amarelo("\n>> Pressione ENTER para retornar ao menu...  "))
                                                op = 0 #retornar ao menu ELEITORES CADASTRADOS
                                                
                                            #=================== MENU REMOVER ELEITOR ====================
                                            case 2:
                                                menu.limpar_terminal()
                                                menu.mostrar_ger_cad_eleitores()
                                                bd.remover_eleitor(valor_busca)
                                                input(cor.amarelo("\n>> Pressione ENTER para retornar ao menu...  "))
                                                op = 0 #retornar ao menu ELEITORES CADASTRADOS

                                            case 0:
                                                msg.alerta("Voltando ao menu...")
                                                time.sleep(1.5)

                                            case _:
                                                msg.erro("Opção inválida.")
                                                time.sleep(1.5)
                                
                                #=================== MENU LISTAR TODOS OS ELEITORES ====================
                                case 2:
                                    menu.limpar_terminal()
                                    menu.mostrar_ger_eleitores_cadastrados()
                                    bd.listar_eleitores()
                                    input(cor.amarelo("\n>> Pressione ENTER para continuar...  "))

                                case 0:
                                    msg.alerta("Voltando ao módulo de Gerenciamento...")
                                    time.sleep(1.5)

                                case _:
                                    msg.erro("Opção inválida.")
                                    time.sleep(1.5)

                    case 0:
                        msg.alerta("Voltando à seleção dos módulos...")
                        time.sleep(1.5)
                    case _:
                        msg.erro("Opção inválida.")
                        time.sleep(1.5)

        #=================== MODULO VOTAÇÃO ====================
        case 2:
            menu.limpar_terminal()
            
            op_vot = -1

            while (op_vot != 0):
                menu.mostrar_vot()
                op_vot = menu.selecionar_opcao()

                match op_vot:
                    
                    #=================== ABRIR VOTAÇÃO ====================
                    case 1:
                        menu.limpar_terminal()
                        menu.mostrar_vot_abertura()
                        
                        print(cor.ciano("Para abrir a votação, entre com as credenciais de um MESÁRIO autorizado:\n"))
                        time.sleep(1)
                        print(cor.ciano("Passo 1 de 3..."))
                        titulo = input("Título do mesário: ").strip()
                        print(cor.ciano("Passo 2 de 3..."))
                        primeiros_cpf = input("4 primeiros dígitos do CPF: ").strip()
                        print(cor.ciano("Passo 3 de 3..."))
                        chave = input("Chave de acesso: ").strip()

                        arquivo_log = mod_vot.abrir_votacao(titulo, primeiros_cpf, chave)

                        if not arquivo_log:
                            msg.erro("Não foi possível abrir a votação.")
                            input(cor.amarelo("\n>> Pressione ENTER para continuar...  "))
                            menu.limpar_terminal()
                            continue
                        
                        menu.limpar_terminal()
                        menu.mostrar_vot_abertura()
                        msg.sucesso("Sistema de votação aberto com sucesso!")
                        input(cor.amarelo("\n>> Pressione ENTER para acessar o menu da urna..."))

                        op_votacao = 0

                        while op_votacao != -1:
                            menu.limpar_terminal()
                            menu.mostrar_vot_menu_votacao()
                            op_votacao = menu.selecionar_opcao()

                            match op_votacao:
                                case 1:
                                    menu.limpar_terminal()
                                    menu.mostrar_vot_votacao()

                                    print(cor.ciano("Para votar, entre com suas credenciais de eleitor:\n"))
                                    time.sleep(1)
                                    print(cor.ciano("Passo 1 de 3..."))
                                    titulo = input("Título do eleitor: ").strip()
                                    print(cor.ciano("Passo 2 de 3..."))
                                    primeiros_cpf = input("4 primeiros dígitos do CPF: ").strip()
                                    print(cor.ciano("Passo 3 de 3..."))
                                    chave = input("Chave de acesso: ").strip()
                                    time.sleep(1)
    
                                    resultado = mod_vot.autenticar_eleitor(titulo, primeiros_cpf, chave)
                                     
                                    if not resultado["sucesso"]:
                                        msg.erro(resultado["mensagem"])
                                        input(cor.amarelo("\n>> Pressione ENTER para tentar novamente...  "))
                                        continue

                                    menu.limpar_terminal()
                                    menu.mostrar_vot_votacao()

                                    votacao_concluida = False
        
                                    while not votacao_concluida:
                                        if resultado["sucesso"]:
                                            msg.sucesso(resultado["mensagem"])
                                            id_eleitor = resultado["id_eleitor"]

                                            print(cor.amarelo("\n>> Carregando lista de candidatos..."))
                                            time.sleep(2)

                                            menu.limpar_terminal()
                                            menu.mostrar_vot_votacao()

                                            menu.mostrar_vot_candidatos()
                                            candidatos = bd.listar_candidatos()
                                            for candidato in candidatos:
                                                print(f"{cor.ciano(f'[{candidato['numero_candidato']}]')} {candidato['nome_candidato']} | {candidato['partido_candidato']}")
                                                
                                            if not candidatos:
                                                input(cor.amarelo("\n>> Pressione ENTER para continuar...  "))
                                                menu.limpar_terminal()
                                                continue
                        
                                            numero_candidato = int(input("\nDigite o número do seu candidato: ").strip())
                
                                            protocolo = mod_vot.registrar_voto(id_eleitor, numero_candidato)
                
                                            if protocolo == "REPETIR":
                                                msg.erro("Você já votou! Não é permitido votar mais de uma vez.")
                                                votacao_concluida = False
                                            elif protocolo:

                                                menu.limpar_terminal()
                                                menu.mostrar_vot_votacao()
                                                msg.sucesso(f"Votação finalizada!")
                                                mod_vot.mostrar_protocolo(protocolo)
                                                input(cor.amarelo("\n>> Pressione ENTER para finalizar...  "))

                                                votacao_concluida = True 
                                            else:
                                                msg.erro("Erro crítico ao registrar o voto.")
                                                votacao_concluida = True
                
                                    else:
                                        msg.erro(resultado["mensagem"])

                                case 2:
                                    menu.limpar_terminal()
                                    menu.mostrar_vot_encerrar()
                                    
                                    print(cor.ciano("Para encerrar a votação, entre com as credenciais de um MESÁRIO autorizado:\n"))
                                    time.sleep(1)

                                    print(cor.ciano("Passo 1 de 3..."))
                                    titulo = input("Título do mesário: ").strip()
                                    print(cor.ciano("Passo 2 de 3..."))
                                    primeiros_cpf = input("4 primeiros dígitos do CPF: ").strip()
                                    print(cor.ciano("Passo 3 de 3..."))
                                    chave = input("Chave de acesso: ").strip().upper() #usar getpass ??

                                    resultado = mod_vot.encerrar_votacao(titulo, primeiros_cpf, chave)

                                    if resultado:
                                        logs.encerramento(arquivo_log)
                                        msg.sucesso("Sistema de votação encerrado.")
                                        time.sleep(1.5)

                                        break
                                    else:
                                        msg.erro("Falha ao encerrar votação.")

                                    input(cor.amarelo("\n>> Pressione ENTER para continuar...  "))

                                case _:
                                    msg.erro("Opção inválida.")

                    #=================== AUDITORIA ====================
                    case 2:
                        menu.limpar_terminal()
                        op_auditoria = -1

                        while (op_auditoria != 0):
                            print(cor.azul("\n█▓▒▒░░░ AUDITORIA DO SISTEMA DE VOTAÇÃO ░░░▒▒▓█"))
                            print(menu.vot_menu_auditoria)
                            op_auditoria = menu.selecionar_opcao()

                            match op_auditoria:
                                case 1:
                                    logs.exibir_logs()
                                case 2:
                                    msg.alerta("[Exibir Protocolos da Votação]")
                                case 0:
                                    msg.alerta("Voltando para o menu anterior...")
                                case _:
                                    msg.erro("Opção inválida.")

                    #=================== RESULTADO ====================
                    case 3:
                        menu.limpar_terminal()
                        op_resultado = -1

                        while (op_resultado != 0):
                            print(cor.azul("\n█▓▒▒░░░ RESULTADO DA VOTAÇÃO ░░░▒▒▓█"))
                            print(menu.vot_menu_resultado)
                            op_resultado = menu.selecionar_opcao()

                            match op_resultado:
                                case 1:
                                    msg.alerta("[Boletim de Urna]")
                                case 2:
                                    msg.alerta("[Estatística de Comparecimento]")
                                case 3:
                                    msg.alerta("[Votos por Partido]")
                                case 4:
                                    msg.alerta("[Validação da Integridade dos Votos]")
                                case 0:
                                    msg.alerta("Voltando para o menu anterior...")
                                case _:
                                    msg.erro("Opção inválida.")
                        
                    case 0:
                        msg.alerta("Voltando à seleção dos módulos...")
                    case _:
                        msg.erro("Opção inválida.")
        
        case 0:
            msg.alerta("Encerrando o programa LAD.PY...")
            time.sleep(1.5)
            menu.limpar_terminal()

        case _:
            msg.erro("Opção inválida.")
            time.sleep(1.5)
        





