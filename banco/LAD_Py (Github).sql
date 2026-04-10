
-- Atributos renomeados para  snake_case:

CREATE TABLE candidatos(
id_candidato INT PRIMARY KEY AUTO_INCREMENT,
nome_candidato VARCHAR(100) NOT NULL,
partido_candidato VARCHAR(50) NOT NULL,
numero_candidato INT NOT NULL UNIQUE);

CREATE TABLE votos(
id_voto INT PRIMARY KEY AUTO_INCREMENT,
id_candidato INT NOT NULL,
protocolo VARCHAR(100) NOT NULL UNIQUE,
data_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato));

INSERT INTO candidatos(nome_candidato, partido_candidato, numero_candidato) VALUES
('João das Neves', 'PN', 33),
('Daene Tardelli', 'PMD', 66);

-- teste de insert em outro horario para verificação do campo "DataHora":
INSERT INTO votos (id_candidato, protocolo) VALUES
(1, 'TESTE003');

SELECT * FROM candidatos;
SELECt *FROM votos;

-- Select de verificação de votos computados individualmente com protocolo e hora:
SELECT votos.protocolo, votos.data_hora, candidatos.nome_candidato, candidatos.numero_candidato
FROM votos
JOIN candidatos ON votos.id_candidato = candidatos.id_candidato;

-- Select para contagem de votos por candidato, mostrando o nome partido e quantidade de votos recebidos:
SELECT candidatos.nome_candidato, candidatos.partido_candidato, COUNT(*)
FROM votos
JOIN candidatos ON candidatos.id_candidato = votos.id_candidato
GROUP BY candidatos.nome_candidato, candidatos.partido_candidato;