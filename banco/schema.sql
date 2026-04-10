USE LAD_Py;
CREATE TABLE IF NOT EXISTS eleitores (
    id_eleitor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    titulo_eleitor VARCHAR(12) NOT NULL UNIQUE,
    cpf VARCHAR(50) NOT NULL UNIQUE,
    chave_acesso VARCHAR(50) NOT NULL,
    is_mesario BOOLEAN NOT NULL DEFAULT FALSE,
    status_voto BOOLEAN DEFAULT FALSE
);
-- Tabelas "candidatos" e "votos" (Marialvo):
CREATE TABLE IF NOT EXISTS candidatos(
id_candidato INT PRIMARY KEY AUTO_INCREMENT,
nome_candidato VARCHAR(100) NOT NULL,
partido_candidato VARCHAR(50) NOT NULL,
numero_candidato INT NOT NULL UNIQUE);

CREATE TABLE IF NOT EXISTS votos(
id_voto INT PRIMARY KEY AUTO_INCREMENT,
id_candidato INT NOT NULL,
protocolo VARCHAR(100) NOT NULL UNIQUE,
data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato));
