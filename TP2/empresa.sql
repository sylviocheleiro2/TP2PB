drop database if exists empresa;
create database empresa;
use empresa;

CREATE TABLE funcionarios (
    ID INT NOT NULL,
    Nome VARCHAR(100),
    Cargo VARCHAR(50),
    Departamento VARCHAR(50),
    Salario DECIMAL(10, 2),
    DataContratacao DATE,
    CargoConfianca INT,
    PRIMARY KEY (ID)
);

INSERT INTO funcionarios (ID, Nome, Cargo, Departamento, Salario, DataContratacao, CargoConfianca)
VALUES
(10, 'Alec do Nascimento', 'Técnico', 'Jurídico', 3000.00, '2023-03-16', 0),
(20, 'Arthur Assis', 'Analista', 'Jurídico', 5000.00, '2020-04-19', 0),
(30, 'Caio Cesar2', 'Técnico', 'Financeiro', 3000.00, '2021-10-01', 0),
(40, 'Daniel da Silva', 'Analista', 'Financeiro', 5000.00, '2022-12-26', 0),
(50, 'Davi de Oliveira', 'Analista', 'TI', 5000.00, '2022-09-23', 0),
(60, 'Gabriel Maia', 'Técnico', 'Financeiro', 3000.00, '2023-12-19', 0),
(70, 'Gabriel Cavalcante', 'Analista', 'TI', 5000.00, '2020-05-09', 0),
(80, 'Igor Cruz', 'Técnico', 'Financeiro', 3000.00, '2024-01-14', 0),
(90, 'João David Castro', 'Coordenador', 'TI', 6000.00, '2024-01-07', 1),
(100, 'João Miguel da Silva', 'Gerente', 'Jurídico', 7500.00, '2021-05-19', 1),
(110, 'João Paulo de Abreu', 'CFO', 'Financeiro', 15000.00, '2021-12-21', 1),
(120, 'Jorge Henrique da Silva', 'Diretor', 'Financeiro', 8500.00, '2022-01-12', 1),
(130, 'Júlia Pereira Santos', 'Analista', 'Jurídico', 5000.00, '2020-10-03', 0),
(140, 'Karoline de Oliveira', 'Técnico', 'Jurídico', 3000.00, '2023-03-15', 0),
(150, 'Kauã Correia', 'Analista', 'Jurídico', 5000.00, '2020-09-09', 0),
(160, 'Kauan Torres', 'Técnico', 'TI', 3000.00, '2020-09-03', 0),
(170, 'Lara Pessanha', 'Analista', 'TI', 5000.00, '2021-11-01', 0),
(180, 'Laura Santos', 'Técnico', 'TI', 3000.00, '2022-09-01', 0),
(190, 'Lauro Andrade', 'CEO', 'Executivo', 30000.00, '2022-08-04', 1),
(200, 'Matheus da Silva', 'Analista', 'Financeiro', 5000.00, '2020-03-22', 0),
(210, 'Miguel Chaves', 'Técnico', 'Financeiro', 3000.00, '2022-04-06', 0),
(220, 'NIcollas Theodoro', 'Técnico', 'TI', 3000.00, '2022-04-11', 0),
(230, 'Pedro Henrique Santos', 'Técnico', 'TI', 3000.00, '2021-06-04', 0),
(240, 'Rayssa da Silva', 'Diretor', 'TI', 8500.00, '2021-04-07', 1),
(250, 'Rebeca Alves', 'Analista', 'TI', 5000.00, '2022-11-29', 0),
(260, 'Tábatha Tavares', 'Técnico', 'TI', 3000.00, '2021-03-21', 0),
(270, 'Vinicius Araujo', 'Analista', 'TI', 5000.00, '2023-08-07', 0),
(280, 'Yan Tavares', 'Técnico', 'TI', 3000.00, '2023-06-16', 0);