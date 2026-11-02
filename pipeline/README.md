# Pipeline ETL — ObservaClima

Este módulo é responsável por todo o processo de Extração, Transformação e Carga (ETL) dos dados meteorológicos.

## Estrutura

- **`extract.py`**: Responsável por consumir a API Open-Meteo e retornar os dados brutos em formato JSON. 
- **`transform.py`**: Responsável por validar, limpar e transformar os dados brutos em um formato estruturado (DataFrame pandas).
- **`validate.py`**: Responsável por validar a integridade dos dados (ex: verificar se não há valores nulos, se as datas estão no formato correto, etc).
- **`load.py`**: Responsável por persistir os dados transformados no banco de dados PostgreSQL.

## Fluxo de dados

- extract.py (dados brutos JSON)
- validate.py (validação)
- transform.py (DataFrame estruturado)
- load.py (PostgreSQL)

## Status Atual

-  `extract.py`: Implementado e testado
-  `validate.py`: A ser implementado
-  `transform.py`: A ser implementado
-  `load.py`: A ser implementado após configuração do PostgreSQL