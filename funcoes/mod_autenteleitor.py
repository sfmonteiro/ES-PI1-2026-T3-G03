from cripto import decifrar 

def autenticar_eleitor(titulo, primeiros_cpf, chave_acesso_input, conexao):
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
    try:
        cursor = conexao.cursor(dictionary=True)
        
        # consulta a base de dados pelo título
        query = "SELECT id_eleitor, cpf, chave_acesso, status_voto, is_mesario FROM eleitores WHERE titulo_eleitor = %s"
        cursor.execute(query, (titulo,))
        eleitor = cursor.fetchone()

        if not eleitor:
            return {"sucesso": False, "mensagem": "Eleitor não encontrado."}

        # decifrar os dados para comparação
        cpf_real = decifrar(eleitor['cpf'], "cpf")
        chave_real = decifrar(eleitor['chave_acesso'], "chave")

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