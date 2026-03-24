# LAD.Py — Sistema de Votação Digital

> Projeto Integrador I — Engenharia de Software · PUC Campinas  
> Prof. Dr. Luã Marcelo Muriana · 2026

---

## Descrição

O **LAD.Py** é um sistema de votação digital desenvolvido exclusivamente para fins didáticos, como parte da disciplina Projeto Integrador I do curso de Engenharia de Software da PUC Campinas.

O sistema é executado via terminal (linha de comando) e integra três áreas do conhecimento:

- **Lógica de Programação em Python** — estruturas de controle, validação de entradas e organização modular
- **Banco de Dados com MySQL** — modelagem relacional, integridade referencial e manipulação de dados
- **Matemática Aplicada** — Cifra de Hill (álgebra linear) para proteção de informações sensíveis

O sistema contempla dois módulos principais: **Gerenciamento** (cadastro e controle de eleitores e candidatos) e **Votação** (abertura, coleta de votos, encerramento e apuração de resultados), com mecanismos de segurança, rastreabilidade via logs e criptografia de dados sensíveis.

> **Aviso:** Este projeto é uma simulação acadêmica e não possui qualquer relação com sistemas eleitorais reais.

---

## Integrantes

| Nome | RA |
|------|--------|
| Gabrielle |  |
| Guilherme |  |
| Marialvo  |  |
| Sara      | 25024107 |
| Sophia    | 25020335 |

---

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python 3.x | Linguagem principal do projeto |
| MySQL | Banco de dados relacional |
| mysql-connector-python | Conexão entre Python e MySQL |
| datetime | Registro de data e hora dos eventos |
| random | Geração de chaves de acesso e protocolos |
| colorama | Colorização da interface no terminal |
| Cifra de Hill | Criptografia de CPF, chave de acesso e protocolo de votação |
| Git + GitHub | Controle de versão e entrega |
| GitHub Projects | Gerenciamento de tarefas e apontamento de esforço |

---

## Estrutura do projeto

```
LAD.Py/
├── lad.py           # Sistema completo — todas as funções e menus
├── schema.sql       # Script de criação das tabelas no MySQL
├── ocorrencias.txt  # Arquivo de log gerado automaticamente em tempo de execução
└── README.md
```

---

## Pré-requisitos

Antes de executar o sistema, certifique-se de ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- Biblioteca `mysql-connector-python`:

```bash
pip install mysql-connector-python colorama
```

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ES-PI1-2026-TURMA-GRUPO.git
cd ES-PI1-2026-TURMA-GRUPO
```

### 2. Configure o banco de dados

Acesse o MySQL e execute o script de criação das tabelas:

```bash
mysql -u root -p < banco/schema.sql
```

### 3. Configure a conexão

No início do arquivo `lad.py`, edite as credenciais do MySQL:

```python
host     = "localhost"
user     = "root"
password = "sua_senha"
database = "ladpy"
```

### 4. Execute o sistema

```bash
python lad.py
```

---

## Funcionalidades

### Módulo de Gerenciamento
- Cadastro de eleitores com validação matemática de CPF e Título de Eleitor
- Geração automática de chave de acesso individual (criptografada)
- Edição, remoção, busca e listagem de eleitores

### Módulo de Votação
- Abertura da urna com autenticação do mesário e Zerézima
- Identificação do eleitor e registro do voto com protocolo único
- Encerramento com dupla confirmação de segurança

### Módulo de Resultados
- Boletim de urna com declaração do vencedor
- Estatísticas de comparecimento e votos por partido
- Validação de integridade entre votos registrados e eleitores que votaram

### Módulo de Auditoria
- Log cronológico de todas as ocorrências críticas (`.txt`)
- Exibição dos protocolos de votação para conferência

---

## Segurança e criptografia

Dados sensíveis são protegidos pela **Cifra de Hill** antes de serem armazenados no banco de dados:

- CPF do eleitor
- Chave de acesso
- Protocolo de votação

> A Cifra de Hill é utilizada aqui com finalidade didática (aprendizado de álgebra linear). Em sistemas reais, recomenda-se SHA-256, AES ou RSA.

---

## Entrega

- **Data limite:** 29 de maio de 2026 às 23h59
- **Formato:** Release no GitHub com tag `1.0.0-final`
- **Repositório:** `ES-PI1-2026-TURMA-GRUPO`

---

## Licença

Projeto acadêmico desenvolvido para fins educacionais — PUC Campinas, 2026.
