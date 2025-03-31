CREATE DATABASE interative_care;
USE interative_care;

CREATE TABLE operadoras (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL UNIQUE,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(50)
);
CREATE TABLE endereco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT,
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(50),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(9),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT,
    ddd CHAR(2),
    telefone VARCHAR(10),
    fax VARCHAR(10),
    endereco_eletronico VARCHAR(255),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
CREATE TABLE representantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT,
    nome VARCHAR(255),
    cargo VARCHAR(50),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
CREATE TABLE comercializacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans INT,
    regiao VARCHAR(255),
    data_registro_ans DATE,
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
select * from operadoras;
SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\operadoras.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ','  -- Ajuste o delimitador conforme necessário
ENCLOSED BY '"'            -- Ajuste o encapsulador conforme necessário
LINES TERMINATED BY '\n'   -- Confirme o terminador de linha
IGNORE 1 LINES             -- Ignora a linha de cabeçalho
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade);