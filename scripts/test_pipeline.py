from datetime import date, timedelta

from pipeline.extract import fetch_historical_data, ExtractError
from pipeline.validate import validate_daily_data, ValidationError
from pipeline.transform import transform_to_dataframe, TransformError


def main():
    # Calcula o intervalo do último trimestre
    end_date = date.today()
    start_date = end_date - timedelta(days=90)
    
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")

    print(f"Pipeline ETL - Recife")
    print(f"Período: {start_str} até {end_str}")
    print("=" * 20)

    # Extract
    print("Extraindo dados da API Open-Meteo")
    try:
        raw_data = fetch_historical_data("recife", start_str, end_str)
        num_days = len(raw_data["daily"]["time"])
        print(f"{num_days} dias extraídos com sucesso.")
    except ExtractError as e:
        print(f"ERRO NA EXTRAÇÃO: {e}")
        return

    # Validate
    print("Validando dados...")
    try:
        validate_daily_data(raw_data)
        print("Dados validados com sucesso.")
    except ValidationError as e:
        print(f"ERRO NA VALIDAÇÃO: {e}")
        return

    # Transform
    print("Transformando dados em DataFrame...")
    try:
        df = transform_to_dataframe(raw_data)
        print(f"DataFrame criado com {len(df)} registros.")
    except TransformError as e:
        print(f"ERRO NA TRANSFORMAÇÃO: {e}")
        return

    # Teste
    print("=" * 20)
    print("=" * 20)
    print("ESTATÍSTICAS DO PERÍODO:")
    print(f"Temperatura máxima média: {df['temp_max'].mean():.1f}°C")
    print(f"Temperatura mínima média: {df['temp_min'].mean():.1f}°C")
    print(f"Temperatura média geral: {df['temp_avg'].mean():.1f}°C")
    print(f"Total de precipitação: {df['precipitation'].sum():.1f} mm")
    print("=" * 20)

    print("\n"+"Amostra dos 5 primeiros registros:")
    print("\n"+df.head().to_string(index=False))

    print("Amostra dos 5 últimos registros:")
    print("\n"+df.tail().to_string(index=False))


if __name__ == "__main__":
    main()