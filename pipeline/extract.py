import requests

# Identificação das cidades
CITIES = {"recife": {
        "latitude": -8.05389,
        "longitude": -34.88111,
        "timezone": "America/Recife",
    }}


# Informações diárias da API
DAILY_VARIABLES = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
]

ARCHIVE_API_URL = "https://archive-api.open-meteo.com/v1/archive"


class ExtractError(Exception):
    # Exceção base para erros de extração de dados
    pass

# Busca a partir do nome da cidade, data inicial e data final daquele histórico de dados, e retorna um dicionário
# com a resposta da API
def fetch_historical_data(city_name: str, start_date: str, end_date: str) -> dict:
    city_name = city_name.lower()
    if city_name not in CITIES:
        raise ExtractError(
            f"Cidade '{city_name}' não configurada."
            f"Disponíveis: {list(CITIES.keys())}"
        )

    city_config = CITIES[city_name]

    # Requisições
    params = {
        "latitude": city_config["latitude"],
        "longitude": city_config["longitude"],
        "start_date": start_date,
        "end_date": end_date,
        "daily": ",".join(DAILY_VARIABLES),
        "timezone": city_config["timezone"],
    }

    # Tratamento de erros pra requisição
    try:
        response = requests.get(ARCHIVE_API_URL, params=params, timeout=30)
        response.raise_for_status()  # lança HTTPError se status for 4xx/5xx
    except requests.ConnectionError:
        raise ExtractError("Falha de conexão com a API Open-Meteo. Verifique sua internet.")
    except requests.Timeout:
        raise ExtractError("A requisição demorou mais de 30 segundos e foi cancelada.")
    except requests.HTTPError as e:
        raise ExtractError(f"A API retornou erro HTTP: {e.response.status_code}")
    except requests.RequestException as e:
        raise ExtractError(f"Erro inesperado na requisição: {e}")

    # Transformar a requisição em JSON
    try:
        data = response.json()
    except ValueError:
        raise ExtractError("A resposta da API não é um JSON válido.")

    # Valida se a chave "daily" tá na lista
    if "daily" not in data:
        raise ExtractError(
            "Resposta da API não contém a chave 'daily'. "
            f"Chaves recebidas: {list(data.keys())}"
        )

    return data