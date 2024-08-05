from conectar_db import *

# Consulta 1: Funcionários que trabalham no departamento de TI
def consulta_departamento_ti(cursor):
    query = """
        SELECT *
        FROM funcionarios
        WHERE Departamento = 'TI'
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 2: Nomes dos funcionários com salário maior que 5.000,00
def consulta_salario_maior(cursor):
    query = """
        SELECT Nome
        FROM funcionarios
        WHERE Salario > 5000.00
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 3: Nome e data de contratação dos funcionários contratados após 01/01/2022
def consulta_contratacao_apos(cursor):
    query = """
        SELECT Nome, DataContratacao
        FROM funcionarios
        WHERE DataContratacao > '2022-01-01'
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 4: Departamento e salário médio de cada departamento
def consulta_salario_medio_departamento(cursor):
    query = """
        SELECT Departamento, AVG(Salario) AS SalarioMedio
        FROM funcionarios
        GROUP BY Departamento
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 5: Nome e cargo dos funcionários que possuem "da Silva" no nome
def consulta_da_silva(cursor):
    query = """
        SELECT Nome, Cargo
        FROM funcionarios
        WHERE Nome LIKE '%da Silva%'
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 6: Funcionários que têm cargos de confiança
def consulta_cargos_confianca(cursor):
    query = """
        SELECT *
        FROM funcionarios
        WHERE CargoConfianca = 1
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 7: Nome e departamento dos analistas
def consulta_analistas(cursor):
    query = """
        SELECT Nome, Departamento
        FROM funcionarios
        WHERE Cargo = 'Analista'
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 8: Nome e salário dos funcionários ordenados de forma decrescente pelo salário
def consulta_salario_decrescente(cursor):
    query = """
        SELECT Nome, Salario
        FROM funcionarios
        ORDER BY Salario DESC
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 9: Nome e ID dos funcionários contratados no ano de 2023
def consulta_contratados_ano(cursor):
    query = """
        SELECT Nome, ID
        FROM funcionarios
        WHERE YEAR(DataContratacao) = 2023
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 10: Nome dos funcionários no departamento Jurídico com salário <= 3000,00
def consulta_juridico_salario(cursor):
    query = """
        SELECT Nome
        FROM funcionarios
        WHERE Departamento = 'Jurídico' AND Salario <= 3000.00
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 11: Nome dos funcionários que são Gerentes ou Diretores
def consulta_gerentes_diretores(cursor):
    query = """
        SELECT Nome
        FROM funcionarios
        WHERE Cargo IN ('Gerente', 'Diretor')
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 12: Nome dos funcionários e anos de experiência (considerando que estamos em 2024)
def consulta_anos_experiencia(cursor):
    query = """
        SELECT Nome, YEAR(CURDATE()) - YEAR(DataContratacao) AS AnosExperiencia
        FROM funcionarios
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 13: Nome e departamento dos funcionários, ordenados pelo nome em ordem alfabética
def consulta_ordenada_nome(cursor):
    query = """
        SELECT Nome, Departamento
        FROM funcionarios
        ORDER BY Nome
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 14: Nome e cargo dos funcionários cujo nome começa com 'João'
def consulta_nome_joao(cursor):
    query = """
        SELECT Nome, Cargo
        FROM funcionarios
        WHERE Nome LIKE 'João%'
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

# Consulta 15: Quantidade de funcionários em cada departamento
def consulta_quantidade_departamento(cursor):
    query = """
        SELECT Departamento, COUNT(*) AS QuantidadeFuncionarios
        FROM funcionarios
        GROUP BY Departamento
    """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado