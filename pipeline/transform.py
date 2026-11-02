import pandas as pd

class TransformError(Exception):
    pass

# Transforma os dados da API em um DF pandas
def transform_to_dataframe(daily_data: dict) -> pd.DataFrame:
    try:
        daily = daily_data["daily"]

        # Cria DF a partir do dicionário
        df = pd.DataFrame({
            "date": daily["time"],
            "temp_max": daily["temperature_2m_max"],
            "temp_min": daily["temperature_2m_min"],
            "precipitation": daily["precipitation_sum"],
        })

        # Converte a coluna date para datetime e ordena de forma crescente
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date").reset_index(drop=True)

        # Calcula a temperatura média e arredonda pra uma casa
        df["temp_avg"] = (df["temp_max"] + df["temp_min"]) / 2
        df["temp_max"] = df["temp_max"].round(1)
        df["temp_min"] = df["temp_min"].round(1)
        df["temp_avg"] = df["temp_avg"].round(1)
        df["precipitation"] = df["precipitation"].round(1)

        return df
    # Para erros na transformação dos dados
    except Exception as e:
        raise TransformError(f"Erro ao transformar dados: {e}")