# ===================================================================================================================
#                                                  BIBLIOTECAS
# ===================================================================================================================

import numpy as np


# ===================================================================================================================
#                                               MÓDULO CRIPTOGRAFIA
# ===================================================================================================================

# Alfabeto alfanumérico usado pela Cifra de Hill:
# A-Z => 0-25 | 0-9 => 26-35
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Matriz codificadora escolhida para a cifra
CODIFICADORA = np.array([[4, 5], [5, 8]])

# Determinante da matriz codificadora
det_c = CODIFICADORA[0][0] * CODIFICADORA[1][1] - CODIFICADORA[0][1] * CODIFICADORA[1][0]

# Procura um múltiplo do determinante cujo resto da divisão por 36 seja 1.
# Esse valor será usado para obter o inverso modular do determinante.
multiplo_det = det_c
while multiplo_det % 36 != 1:
    multiplo_det += det_c

# Inverso modular do determinante no módulo 36
inv_mod_det = multiplo_det // det_c

# Matriz adjunta da codificadora
adj_c = np.array([
    [CODIFICADORA[1][1], -CODIFICADORA[0][1]],
    [-CODIFICADORA[1][0], CODIFICADORA[0][0]]
])

# Matriz decodificadora (inversa modular da codificadora no módulo 36)
DECODIFICADORA = (adj_c * inv_mod_det) % 36


def cifrar(texto):
    """
    Criptografa uma string alfanumérica usando a Cifra de Hill.

    Args:
        texto (str): String alfanumérica a ser criptografada.

    Returns:
        str | bool: Retorna a string criptografada ou False em caso de erro.
    """
    texto = texto.upper()
    texto_novo = ""

    # Verifica se todos os caracteres pertencem ao alfabeto permitido
    for caractere in texto:
        if caractere not in ALFABETO:
            return False

    # Adiciona padding caso a quantidade de caracteres seja ímpar
    if len(texto) % 2 != 0:
        texto += "0"

    # Processa o texto em blocos de 2 caracteres
    for i in range(0, len(texto), 2):
        valor1 = ALFABETO.index(texto[i])
        valor2 = ALFABETO.index(texto[i + 1])

        # Aplica a matriz codificadora e reduz os resultados ao módulo 36
        novo1 = (CODIFICADORA[0][0] * valor1 + CODIFICADORA[0][1] * valor2) % 36
        novo2 = (CODIFICADORA[1][0] * valor1 + CODIFICADORA[1][1] * valor2) % 36

        texto_novo += ALFABETO[novo1]
        texto_novo += ALFABETO[novo2]

    return texto_novo


def decifrar(texto, tipo_dado):
    """
    Descriptografa uma string alfanumérica usando a matriz inversa da Cifra de Hill.

    Args:
        texto (str): String alfanumérica criptografada.
        tipo_dado (str): Tipo do dado criptografado ("cpf", "chave" ou "protocolo").

    Returns:
        str | bool: Retorna a string descriptografada ou False em caso de erro.
    """
    texto = texto.upper()
    texto_novo = ""

    # Tamanhos originais dos dados criptografados
    tamanhos = {
        "cpf": 11,
        "chave": 7,
        "protocolo": 12
    }

    tipo_dado = tipo_dado.lower()

    # Verifica se o tipo do dado informado é válido
    if tipo_dado not in tamanhos:
        return False

    tamanho_original = tamanhos[tipo_dado]

    # Verifica se todos os caracteres pertencem ao alfabeto permitido
    for caractere in texto:
        if caractere not in ALFABETO:
            return False

    # O texto criptografado deve ter quantidade par de caracteres
    if len(texto) % 2 != 0:
        return False

    # Processa o texto em blocos de 2 caracteres
    for i in range(0, len(texto), 2):
        valor1 = ALFABETO.index(texto[i])
        valor2 = ALFABETO.index(texto[i + 1])

        # Aplica a matriz decodificadora e reduz os resultados ao módulo 36
        novo1 = (DECODIFICADORA[0][0] * valor1 + DECODIFICADORA[0][1] * valor2) % 36
        novo2 = (DECODIFICADORA[1][0] * valor1 + DECODIFICADORA[1][1] * valor2) % 36

        texto_novo += ALFABETO[novo1]
        texto_novo += ALFABETO[novo2]

    # Remove o padding com base no tamanho original do dado
    return texto_novo[:tamanho_original]