# ObservaClima — Documento de Escopo do Projeto

## 1. Visão Geral
O ObservaClima é uma plataforma web desenvolvida para coleta, armazenamento, processamento e visualização de dados meteorológicos. O sistema atua como uma ponte entre dados brutos de APIs públicas e o usuário final, transformando informações técnicas em gráficos e indicadores de fácil compreensão, auxiliando na análise de tendências climáticas e no acompanhamento do histórico e da previsão do tempo de uma região específica.

## 2. Objetivos
### 2.1. Objetivo Geral
Desenvolver um sistema web funcional para monitoramento climático local, integrando fontes de dados externas a um banco de dados próprio e apresentando as informações de forma visual e acessível.


## 3. Requisitos Funcionais (RF)
- **RF01:** O sistema deve permitir o cadastro, login e logout de usuários.
- **RF02:** O sistema deve consumir a API Open-Meteo para obter dados históricos (90 dias) e de previsão (7 dias) de Recife.
- **RF03:** O sistema deve validar e armazenar os dados recebidos em um banco de dados PostgreSQL.
- **RF04:** O sistema deve calcular indicadores básicos, como média de temperatura e volume total de precipitação do período consultado.
- **RF05:** O sistema deve disponibilizar os dados através de uma API REST própria (Django REST Framework).
- **RF06:** O sistema deve exibir um dashboard web com gráficos interativos das variáveis climáticas ao longo do tempo.

## 4. Requisitos Não Funcionais (RNF)
- **RNF01 (Desempenho):** O dashboard deve carregar e renderizar os gráficos em menos de 3 segundos em uma conexão de banda larga padrão.
- **RNF02 (Usabilidade):** A interface do dashboard deve ser responsiva, adaptando-se razoavelmente a telas de dispositivos móveis, embora o foco de desenvolvimento seja a experiência em desktop.
- **RNF03 (Tecnologia):** O backend deve ser desenvolvido em Python (Django + Django REST Framework), o banco de dados em PostgreSQL e o frontend com HTML, CSS, JavaScript e uma biblioteca de gráficos (ex: Chart.js).
