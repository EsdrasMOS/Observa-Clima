# Observa Clima

Plataforma web para coleta, armazenamento, processamento e visualização de dados meteorológicos da cidade de Recife/PE.

## Objetivo

O Observa Clima atua como uma ponte entre dados brutos de APIs públicas (Open-Meteo) e o usuário final, transformando informações técnicas em gráficos e indicadores de fácil compreensão, auxiliando na análise de tendências climáticas e no acompanhamento do histórico e da previsão do tempo.

## Tecnologias 

- **Backend:** Python 3.13, Django 6.1, Django REST Framework 3.18
- **Banco de Dados:** PostgreSQL
- **Pipeline ETL:** Requests, Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript, Chart.js (a ser implementado)

## Instalação

### Pré-requisitos

- Python 3.13+
- PostgreSQL (a ser configurado na Etapa 5)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Projeto-de-Estagio.git
cd Projeto-de-Estagio
```

2. Crie e ative o ambiente virtual:
````bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# ou
source .venv/bin/activate      # Linux/Mac
````

3. Instale as dependências no terminal:
````bash
pip install -r requirements.txt
````

4. Configure o Pipeline ETL (em desenvolvimento)
````bash
python -m scripts.test_extract
````

5. Rode o servidor Django (a ser implementado)
````bash
python manage.py runserver
````


## Funcionalidades

- Extração de dados históricos da API Open-Meteo
- Transformação e validação dos dados
- Armazenamento em PostgreSQL
- API REST para consulta de dados
- Dashboard com gráficos interativos
- Sistema de autenticação de usuários

## Etapas concluídas:
* Definição do escopo
* Configuração do ambiente
* Módulo de extração de dados (pipeline/extract.py)
* Pipeline ETL completo (transform + load)
* Configuração do PostgreSQL

## Próximas etapas:
* Desenvolvimento do backend Django
* Implementação do dashboard

## Documentação
- [Documento de Escopo]("docs\escopo.md")
- [Pipeline ETL](pipeline\README.md)

## Autor
Desenvolvido como projeto de estágio acadêmico, por Esdras Matheus, Guilherme Lira, João Victor Souza e Kephanny Medeiros.

## Licença
Este projeto está sob a licença [MIT license]("LICENSE"). 