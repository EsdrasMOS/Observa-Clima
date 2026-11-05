# Observa Clima — Documento de Escopo e Evolução do Projeto

## 1. Visão Geral
O Observa Clima é uma plataforma web desenvolvida para coleta, armazenamento, processamento, análise e visualização de dados meteorológicos. O sistema atua como uma ponte entre dados brutos de APIs públicas (Open-Meteo) e o usuário final, transformando informações técnicas em indicadores e gráficos de fácil compreensão, auxiliando na análise de tendências climáticas e no acompanhamento do histórico de uma região específica.

## 2. Objetivos
### 2.1. Objetivo Geral
Desenvolver um sistema web funcional e robusto para monitoramento climático local, integrando fontes de dados externas a um banco de dados relacional e apresentando as informações de forma visual, acessível e analítica.

### 2.2. Objetivos Específicos
- Implementar um pipeline de extração, transformação e carga (ETL) automatizado a partir da API Open-Meteo.
- Persistir os dados históricos e de previsão em um banco de dados relacional (PostgreSQL).
- Desenvolver uma API RESTful documentada para disponibilizar os dados processados.
- Calcular indicadores meteorológicos avançados (médias móveis, extremos e agregações temporais).
- Criar um dashboard web com gráficos interativos (temperatura, umidade e precipitação).
- Implementar um sistema básico de autenticação de usuários.

## 3. Público-Alvo
- **Primário (Atual):** Avaliadores acadêmicos e professores da disciplina de estágio.
- **Secundário (Visão Futura):** Meteorologistas, estudantes e público geral interessado no histórico e previsão do tempo local.
- **Nível Técnico:** Leigo a intermediário (a interface deve ser intuitiva, sem exigir conhecimento técnico para interpretação dos gráficos).

## 4. Escopo Incluído (O que o sistema faz)
- **Localidade:** Cidade de Recife/PE.
- **Período de Dados:** 
  - Histórico: Último trimestre (aproximadamente 90 dias).
  - Previsão: Próximos 7 dias.
- **Variáveis Climáticas:** Temperatura (máxima, mínima, média) e Precipitação.
- **Funcionalidades Implementadas/Em Desenvolvimento:** Pipeline ETL modular, banco de dados PostgreSQL, API REST com paginação e endpoints de análise, e sistema de autenticação (planejado).

## 5. Requisitos Funcionais (RF)
- **RF01:** O sistema deve permitir o cadastro, login e logout de usuários.
- **RF02:** O sistema deve consumir a API Open-Meteo para obter dados históricos (90 dias) de Recife.
- **RF03:** O sistema deve validar (checagem de nulos e consistência) e armazenar os dados recebidos em um banco de dados PostgreSQL.
- **RF04:** O sistema deve calcular indicadores básicos (média, máx, mín, total de chuva) e avançados (média móvel de 7 dias, agregação mensal de chuva, identificação de dias extremos).
- **RF05:** O sistema deve disponibilizar os dados através de uma API REST própria (Django REST Framework), com paginação e formatos padronizados.
- **RF06:** O sistema deve exibir um dashboard web com gráficos interativos das variáveis climáticas ao longo do tempo.

## 6. Requisitos Não Funcionais (RNF)
- **RNF01 (Desempenho):** O dashboard e a API devem responder em menos de 2 segundos em uma conexão de banda larga padrão.
- **RNF02 (Usabilidade):** A interface do dashboard deve ser responsiva, adaptando-se a telas de dispositivos móveis.
- **RNF03 (Tecnologia):** Backend em Python (Django + DRF), Banco em PostgreSQL, Pipeline com Pandas/Requests, Frontend com HTML/CSS/JS e Chart.js.
- **RNF04 (Segurança):** Credenciais de banco de dados e chaves de API devem ser gerenciadas via variáveis de ambiente (`.env`), nunca hardcoded.

## 7. Critérios de Aceitação
- O pipeline ETL executa do início ao fim sem erros, salvando 90+ registros no PostgreSQL.
- A API retorna dados JSON válidos nos endpoints `/api/weather/`, `/api/weather/stats/`, `/api/weather/extremes/` e `/api/weather/monthly/`.
- O usuário consegue visualizar os gráficos no dashboard com dados reais do banco.

## 8. Entregáveis
- [x] Repositório GitHub com o código-fonte versionado e documentado.
- [x] Documento de escopo e arquitetura do sistema (este arquivo).
- [x] Pipeline ETL funcional (Extract, Validate, Transform, Load).
- [x] Banco de dados PostgreSQL configurado e populado.
- [x] API REST desenvolvida e testada.
- [ ] Dashboard web integrado.
- [ ] Sistema de autenticação e automatização (Cron/Task Scheduler).

---

## 9. Registro de Evolução do Projeto (Diário de Bordo)

| Etapa | Descrição | Status |
|-------|-----------|--------|
| **1** | Definição do escopo e requisitos | Concluído |
| **2** | Módulo de extração da API Open-Meteo (`extract.py`) | Concluído |
| **3** | Estruturação do repositório (`.gitignore`, READMEs) | Concluído |
| **4** | Pipeline ETL: Validação e Transformação (Pandas) | Concluído |
| **5** | Instalação e configuração do PostgreSQL + `.env` | Concluído |
| **6** | Criação do projeto Django e integração com o banco | Concluído |
| **7** | Modelagem de dados (`WeatherRecord`) e carga (Load) | Concluído |
| **8** | Desenvolvimento da API REST (DRF) com endpoints básicos | Concluído |
| **9** | Implementação de indicadores avançados | Em andamento |
| **10** | Integração com o Dashboard (Frontend + Chart.js) | Pendente |
| **11** | Automatização das coletas e testes finais | Pendente |