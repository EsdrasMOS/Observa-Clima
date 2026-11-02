from datetime import date, timedelta

from pipeline.extract import fetch_historical_data, ExtractError


def main():
    # Calcula o intervalo do último trimestre
    end_date = date.today()
    start_date = end_date - timedelta(days=90)

    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")

    print(f"Buscando dados de Recife de {start_str} até {end_str}...")
    print("-" * 25)

    try:
        data = fetch_historical_data("recife", start_str, end_str)
    except ExtractError as e:
        print(f"ERRO: {e}")
        return

    # Informações gerais da resposta
    daily = data["daily"]
    num_days = len(daily["time"])

    print(f"Cidade: Recife")
    print(f"Período: {start_str} até {end_str}")
    print(f"Dias recebidos: {num_days}")
    print(f"Variáveis: {list(daily.keys())}")
    print("-" * 25)
    
    # Exibe os 3 primeiros registros como amostra
    print("Amostra dos 3 primeiros dias:")
    for i in range(min(3, num_days)):
        print(f"  {daily['time'][i]} | Max: {daily['temperature_2m_max'][i]}°C | Min: {daily['temperature_2m_min'][i]}°C | Chuva: {daily['precipitation_sum'][i]} mm")

# Exibe os 3 últimos registrod
    print("\nAmostra dos 3 últimos dias:")
    for i in range(max(0, num_days - 3), num_days):
        print(f"  {daily['time'][i]} | Max: {daily['temperature_2m_max'][i]}°C | Min: {daily['temperature_2m_min'][i]}°C | Chuva: {daily['precipitation_sum'][i]} mm")

    print("-" * 25)
    print("Extração concluída com sucesso!")


if __name__ == "__main__":
    main()