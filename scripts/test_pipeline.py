from datetime import date, timedelta

from pipeline.extract import fetch_historical_data, ExtractError
from pipeline.validate import validate_daily_data, ValidationError
from pipeline.transform import transform_to_dataframe, TransformError
from pipeline.load import load_to_database, LoadError


def main():
    # Calcula o intervalo do último trimestre
    end_date = date.today()
    start_date = end_date - timedelta(days=90)

    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")

    print("Pipeline ETL Completo - Recife")
    print(f"Período: {start_str} até {end_str}")
    print("=" * 20)

    # Extract
    print("\nExtraindo dados da API Open-Meteo...")
    try:
        raw_data = fetch_historical_data("recife", start_str, end_str)
        num_days = len(raw_data["daily"]["time"])
        print(f"{num_days} dias extraídos com sucesso.")
    except ExtractError as e:
        print(f"ERRO NA EXTRAÇÃO: {e}")
        return

    # Validate
    print("\nValidando dados...")
    try:
        validate_daily_data(raw_data)
        print("Dados validados com sucesso.")
    except ValidationError as e:
        print(f"ERRO NA VALIDAÇÃO: {e}")
        return

    # Transform
    print("\nTransformando dados em DataFrame...")
    try:
        df = transform_to_dataframe(raw_data)
        print(f"DataFrame criado com {len(df)} registros.")
    except TransformError as e:
        print(f"ERRO NA TRANSFORMAÇÃO: {e}")
        return

    # Load
    print("\nCarregando dados no banco de dados PostgreSQL...")
    try:
        records_saved = load_to_database(df, city_name="Recife")
        print(f"{records_saved} registros salvos/atualizados no banco.")
    except LoadError as e:
        print(f"ERRO NA CARGA: {e}")
        return

    print("\n" + "=" * 20)
    print("RESUMO GERAL:")
    print(f"Total de registros processados: {records_saved}")
    print("=" * 20)


if __name__ == "__main__":
    main()