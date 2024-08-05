import mysql.connector

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="sylvio123",
            database="empresa"  # Nome do banco de dados criado
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None