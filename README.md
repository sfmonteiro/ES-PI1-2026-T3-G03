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

O sistema contempla dois módulos principais: **Gerenciamento** (cadastro e controle de eleitores) e **Votação** (abertura, coleta de votos, encerramento e apuração de resultados), com mecanismos de segurança, rastreabilidade via logs e criptografia de dados sensíveis.

> **Aviso:** Este projeto é uma simulação acadêmica e não possui qualquer relação com sistemas eleitorais reais.

---

## Integrantes

| Nome | RA |
|------|--------|
| Gabrielle Mota de Souza Pinto           | 25024276 |
| Guilherme Mascarenhas Placido Correa    | 25020685 |
| Marialvo Correa de Freitas Jr           | 25020823 |
| Sara Fernandes Monteiro                 | 25024107 |
| Sophia Victoria Martins Fernandes       | 25020335 |

---

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python 3.x | Linguagem principal do projeto |
| MySQL | Banco de dados relacional |
| mysql-connector-python | Conexão entre Python e MySQL |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| datetime | Registro de data e hora dos eventos |
| random | Geração de chaves de acesso e protocolos |
| Cifra de Hill | Criptografia de CPF, chave de acesso e protocolo de votação |
| Git + GitHub | Controle de versão e entrega |
| GitHub Projects | Gerenciamento de tarefas e apontamento de esforço |

---

## Estrutura do projeto

```
LAD.Py/
├── main.py                  # Ponto de entrada do sistema e menus
├── funcoes/
│   ├── bd.py                # Conexão e operações com o banco de dados
│   ├── mod_vot.py           # Lógica do módulo de votação
│   ├── mod_ger.py           # Lógica do módulo de gerenciamento
│   ├── mod_validacao.py     # Validação matemática de CPF e título
│   ├── cripto.py            # Cifra de Hill — criptografia dos dados
│   ├── logs.py              # Registro de ocorrências críticas
│   ├── menu.py              # Exibição de menus e funções auxiliares
│   ├── cor.py               # Cores no terminal
│   └── msg.py               # Mensagens padronizadas (erro, alerta, sucesso)
├── schema.sql               # Script de criação das tabelas no MySQL
├── .env                     # Credenciais do banco de dados (não versionado)
├── .env.example             # Exemplo de configuração do .env
└── README.md
```

---

## Pré-requisitos

Antes de executar o sistema, certifique-se de ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- Dependências Python:

```bash
pip install mysql-connector-python python-dotenv
```

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/sfmonteiro/ES-PI1-2026-T3-G03.git
cd ES-PI1-2026-T3-G03
```

### 2. Configure o banco de dados

Acesse o MySQL e execute o script de criação das tabelas:

```bash
mysql -u root -p < schema.sql
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as credenciais do banco:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=LAD_Py
```

### 4. Execute o sistema

```bash
python main.py
```

---

## Funcionalidades

### Módulo de Gerenciamento
- Cadastro de eleitores com validação matemática de CPF e Título de Eleitor
- Geração automática de chave de acesso individual (criptografada via Cifra de Hill)
- Edição, remoção, busca por CPF ou título, e listagem de todos os eleitores

### Módulo de Votação
- Abertura da urna com autenticação do mesário
- Zerézima obrigatória com exibição de todos os candidatos com zero votos
- Identificação do eleitor com verificação de voto duplo
- Registro do voto com protocolo único gerado e criptografado
- Suporte a voto nulo
- Encerramento com dupla confirmação de segurança pelo mesário

### Módulo de Resultados
- Boletim de urna com declaração do vencedor (ou empate)
- Estatísticas de comparecimento com percentual de participação
- Votos por partido
- Validação de integridade entre votos registrados e eleitores com status "Já Votou"

### Módulo de Auditoria
- Log cronológico de todas as ocorrências críticas em arquivo `.txt`
- Exibição dos protocolos de votação em ordem alfabética para conferência

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
- **Repositório:** [ES-PI1-2026-T3-G03](https://github.com/sfmonteiro/ES-PI1-2026-T3-G03)

---

## Licença

Projeto acadêmico desenvolvido para fins educacionais — PUC Campinas, 2026.
