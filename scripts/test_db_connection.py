import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


def main():
    # Carrega as variáveis do arquivo .env
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(env_path)

    # Lê as variáveis
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    print("Teste de conexão com PostgreSQL")
    print("=" * 20)

    # Verifica se todas as variáveis foram carregadas
    if not all([db_host, db_port, db_name, db_user, db_password]):
        print("ERRO: Variáveis de ambiente não encontradas no .env")
        print(f"DB_HOST: {db_host}")
        print(f"DB_PORT: {db_port}")
        print(f"DB_NAME: {db_name}")
        print(f"DB_USER: {db_user}")
        print(f"DB_PASSWORD: {'***' if db_password else 'NÃO DEFINIDO'}")
        return

    print(f"Host: {db_host}")
    print(f"Porta: {db_port}")
    print(f"Banco: {db_name}")
    print(f"Usuário: {db_user}")
    print("-" * 60)

    # Tenta conectar ao banco
    try:
        print("\nTentando conectar ao banco...")
        conn = psycopg.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        print("Conexão estabelecida com sucesso!")

    # Query simples para testar
        print("\nExecutando query de teste...")
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(f"Versão do PostgreSQL: {version}")

    # Fecha a conexão
        cur.close()
        conn.close()
        print("\nConexão fechada com sucesso.")

    except psycopg.OperationalError as e:
        print(f"ERRO DE CONEXÃO: {e}")
        print("\nPossíveis causas:")
        print("- O serviço do PostgreSQL não está rodando")
        print("- Credenciais incorretas no .env")
        print("- Firewall bloqueando a porta 5432")
        print("- O banco de dados não foi criado")
    except Exception as e:
        print(f"ERRO INESPERADO: {e}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()