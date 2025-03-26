-- Criar o banco de dados
CREATE DATABASE interative_care;
USE interative_care;

-- Tabela para Operadoras
CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_operadora INT NOT NULL,
    nome VARCHAR(255),
    cnpj VARCHAR(20),
    status_operadora VARCHAR(20),
    tipo_operadora VARCHAR(50)
    -- outras colunas se necessário
);

-- Tabela para Demonstracoes Contabeis
CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_operadora INT,
    ano INT,
    trimestre INT,
    eventos_sinistros_conhecidos DECIMAL(15, 2)
    -- outras colunas conforme necessária
);
LOAD DATA LOCAL INFILE 'C:/Users/Admin/Documents/Processo Seletivo Estagio/banco_de_dados/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(codigo_operadora, nome, cnpj, status_operadora, tipo_operadora);
