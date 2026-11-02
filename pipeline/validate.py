class ValidationError(Exception):
    pass

def validate_daily_data(daily_data: dict) -> None:
    #  Verifica se daily existe
    if "daily" not in daily_data:
        raise ValidationError("Dados não contêm a chave 'daily'.")

    daily = daily_data["daily"]

    # Verifica se as variáveis estão em daily
    required_keys = ["time", "temperature_2m_max", "temperature_2m_min", "precipitation_sum"]
    missing_keys = [key for key in required_keys if key not in daily]
    if missing_keys:
        raise ValidationError(f"Variáveis ausentes nos dados: {missing_keys}")

    # Verifica se todas as listas tem o mesmo tamanho
    lengths = {key: len(daily[key]) for key in required_keys}
    if len(set(lengths.values())) > 1:
        raise ValidationError(f"Listas de dados tem tamanhos diferentes: {lengths}")

    # Verifica se tem pelo menos um registro
    if lengths["time"] == 0:
        raise ValidationError("Nenhum registro de dados encontrado.")

    # Verifica valores nulos ou inválidos
    for i in range(lengths["time"]):
        temp_max = daily["temperature_2m_max"][i]
        temp_min = daily["temperature_2m_min"][i]
        precip = daily["precipitation_sum"][i]

    # Verifica se algum valor é None
        if temp_max is None or temp_min is None or precip is None:
            raise ValidationError(f"Valor nulo encontrado no índice {i}. "
                                  f"temp_max={temp_max}, temp_min={temp_min}, precip={precip}"
            )

    # Temperatura máxima é maior ou igual a temperatura mínima
        if temp_max < temp_min:
            raise ValidationError(f"Temperatura máxima ({temp_max}) menor que mínima ({temp_min}) no índice {i}.")

    # Precipitação maior que 0
        if precip < 0:
            raise ValidationError(f"Precipitação negativa ({precip}) no índice {i}.")