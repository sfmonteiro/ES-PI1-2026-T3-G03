def validar_cpf(cpf):
    """
    Realiza a validação matemática do CPF através dos dígitos verificadores.

    Verifica se o CPF possui 11 dígitos, se não são todos iguais e se os
    dígitos verificadores calculados condizem com os informados.

    Args:
        cpf (str): O número do CPF contendo apenas algarismos.

    Returns:
        bool: Retorna True se o CPF for válido, False caso contrário.
    """
  
    # Verifica se tem 11 digitos e se não são todos iguais (ex: 111.111.111-11)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Primeiro Dígito: Multiplica os 9 primeiros dígitos por uma sequência decrescente de 10 a 2.
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    # Somamos os resultados e calculamos o resto da divisão por 11:
    resto = soma % 11
    # Regra: Se o resto for menor que 2, o dígito é 0. Se for 2 ou mais, o dígito é 11−resto. Se o resultado dessa subtração for 10, o dígito também será 0.
    dv1 = 0 if resto < 2 else 11 - resto
    if dv1 >= 10: dv1 = 0

    # Cálculo do segundo dígito
    # Incluímos o primeiro dígito verificador e multiplicamos os 10 dígitos por uma sequência de 11 a 2:
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    # se o resto for menor que 2, o primeiro dígito verificador é 0. Se for 2 ou mais, o dígito é 11−resto. Se o resultado dessa subtração for 10, o dígito também será 0.
    dv2 = 0 if resto < 2 else 11 - resto
    if dv2 >= 10: dv2 = 0

    # Compara os dois últimos dígitos do CPF informado (cpf[-2:]) com os dois dígitos (dv1 e dv2). Se forem iguais, o CPF é válido.
    return cpf[-2:] == f"{dv1}{dv2}"

def validar_titulo(titulo):
    """
    Valida o Título de Eleitor calculando os dígitos verificadores conforme a UF.

    O cálculo utiliza pesos específicos para o número sequencial e para 
    o código da Unidade Federativa (UF).

    Args:
        titulo (str): O número do Título de Eleitor com 12 dígitos.

    Returns:
        bool: Retorna True se o título for válido, False caso contrário.
    """

    # Verifica se o título tem exatamente 12 dígitos
    if len(titulo) != 12:
        return False

    # Fatia as strings, os 8 primeiros dígitos formam o número sequencial, os próximos 2 dígitos representam a UF e os últimos 2 são os dígitos verificadores informados.
    sequencial = titulo[:8]
    uf = titulo[8:10]
    dv_informado = titulo[10:]

    # Multiplica os algarismos do sequencial pelos pesos 2, 3, 4, 5, 6, 7, 8 e 9.
    soma = sum(int(sequencial[i]) * (i + 2) for i in range(8))
    resto = soma % 11
    # Calcula o primeiro DV como o resto da divisão por 11. Se o resto for 10, o dígito vira 0. Para SP e MG, se o resto for 0, o dígito é 1.
    dv1 = 0 if resto == 10 else resto
    # Regra SP/MG
    if uf in ['01', '02'] and resto == 0:
        dv1 = 1

    # Segundo DV (UF + primeiro DV). unindo os dígitos da UF com o primeiro DV que acabamos de descobrir, formando uma nova sequência de 4 dígitos (ex: UF=01 e DV1=5 -> "015"). 
    # Multiplicamos essa sequência pelos pesos 7, 8, 9.
    parte2 = uf + str(dv1)
    soma = sum(int(parte2[i]) * (i + 7) for i in range(3))
    resto = soma % 11
    dv2 = 0 if resto == 10 else resto
    # Regra SP/MG
    if uf in ['01', '02'] and resto == 0:
        dv2 = 1
    
    # Verifica se os dois últimos dígitos do título batem com o que calculamos.
    return dv_informado == f"{dv1}{dv2}"