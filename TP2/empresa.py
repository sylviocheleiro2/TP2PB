from conectar_db import conectar_bd
from crud_db import *

def exibir_menu():
    print("\n### Menu de Consultas ###")
    print("1. Funcionários do departamento de TI")
    print("2. Nomes dos funcionários com salário maior que 5.000,00")
    print("3. Nome e data de contratação dos funcionários contratados após 01/01/2022")
    print("4. Departamento e salário médio de cada departamento")
    print("5. Nome e cargo dos funcionários que possuem 'da Silva' no nome")
    print("6. Funcionários que têm cargos de confiança")
    print("7. Nome e departamento dos analistas")
    print("8. Nome e salário dos funcionários ordenados de forma decrescente pelo salário")
    print("9. Nome e ID dos funcionários contratados no ano de 2023")
    print("10. Nome dos funcionários no departamento Jurídico com salário <= 3000,00")
    print("11. Nome dos funcionários que são Gerentes ou Diretores")
    print("12. Nome dos funcionários e anos de experiência")
    print("13. Nome e departamento dos funcionários, ordenados pelo nome em ordem alfabética")
    print("14. Nome e cargo dos funcionários cujo nome começa com 'João'")
    print("15. Quantidade de funcionários em cada departamento")
    print("0. Sair")

def main():
    # Conectar ao banco de dados
    conn = conectar_bd()
    if not conn:
        return
    
    # Criar um cursor para executar as consultas
    cursor = conn.cursor()

    try:
        while True:
            exibir_menu()
            opcao = input("\nDigite o número da consulta que deseja executar (ou 0 para sair): ")

            if opcao == "0":
                print("Encerrando programa...")
                break
            elif opcao == "1":
                resultado = consulta_departamento_ti(cursor)
            elif opcao == "2":
                resultado = consulta_salario_maior(cursor)
            elif opcao == "3":
                resultado = consulta_contratacao_apos(cursor)
            elif opcao == "4":
                resultado = consulta_salario_medio_departamento(cursor)
            elif opcao == "5":
                resultado = consulta_da_silva(cursor)
            elif opcao == "6":
                resultado = consulta_cargos_confianca(cursor)
            elif opcao == "7":
                resultado = consulta_analistas(cursor)
            elif opcao == "8":
                resultado = consulta_salario_decrescente(cursor)
            elif opcao == "9":
                resultado = consulta_contratados_ano(cursor)
            elif opcao == "10":
                resultado = consulta_juridico_salario(cursor)
            elif opcao == "11":
                resultado = consulta_gerentes_diretores(cursor)
            elif opcao == "12":
                resultado = consulta_anos_experiencia(cursor)
                for row in resultado:
                    print(f"{row[0]} - {row[1]} anos de experiência")
                continue
            elif opcao == "13":
                resultado = consulta_ordenada_nome(cursor)
            elif opcao == "14":
                resultado = consulta_nome_joao(cursor)
            elif opcao == "15":
                resultado = consulta_quantidade_departamento(cursor)
                for row in resultado:
                    print(f"{row[0]}: {row[1]} funcionários")
                continue
            else:
                print("Opção inválida. Tente novamente.")
                continue
            
            # Imprimir resultado das consultas que retornam dados
            for row in resultado:
                print(row)

    except mysql.connector.Error as err:
        print(f"Erro ao executar consulta: {err}")

    finally:
        # Fechar cursor e conexão com o banco de dados
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
