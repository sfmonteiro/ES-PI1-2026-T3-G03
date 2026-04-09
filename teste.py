from funcoes.bd import cadastrar_eleitor

def conectar():
    print("[TESTE] Simulando conexão com o banco...")
    return MockConnection()

class MockConnection:
    def cursor(self): return MockCursor()
    def commit(self): pass
    def is_connected(self): return True
    def close(self): pass

class MockCursor:
    def execute(self, query, valores):
        print(f"[TESTE] Executando SQL: {query[:30]}...")
        # Simula uma colisão de chave uma única vez para testar seu loop!
        if "chave_duplicada" in str(valores):
            from mysql.connector import IntegrityError
            raise IntegrityError("Duplicate entry for key 'chave_acesso'")
    def close(self): pass

def testar_cadastro_isolado():
    print("\n=== TESTE 1: CPF INVÁLIDO ===")
    # Deve retornar False e nem tentar "conectar"
    cadastrar_eleitor("André Silva", "000", "111", False) 

    print("\n=== TESTE 2: CADASTRO COM SUCESSO ===")
    # Deve validar, gerar chave, cifrar e "salvar"
    # Use um CPF e Título válidos que você criou na Sprint 2 
    cadastrar_eleitor("André Silva", "004356870906", "12345678909", False)

    print("\n=== TESTE FINALIZADO ===")

if __name__ == "__main__":
    testar_cadastro_isolado()