# ObservaClima — Documento de Escopo do Projeto

## 1. Visão Geral
O ObservaClima é uma plataforma web desenvolvida para coleta, armazenamento, processamento e visualização de dados meteorológicos. O sistema atua como uma ponte entre dados brutos de APIs públicas e o usuário final, transformando informações técnicas em gráficos e indicadores de fácil compreensão, auxiliando na análise de tendências climáticas e no acompanhamento do histórico e da previsão do tempo de uma região específica.

## 2. Objetivos
### 2.1. Objetivo Geral
Desenvolver um sistema web funcional para monitoramento climático local, integrando fontes de dados externas a um banco de dados próprio e apresentando as informações de forma visual e acessível.

### 2.2. Objetivos Específicos
- Implementar um pipeline de extração de dados (ETL) a partir da API Open-Meteo.
- Persistir os dados históricos e de previsão em um banco de dados relacional (PostgreSQL).
- Desenvolver uma API RESTful para disponibilizar os dados processados.
- Criar um dashboard web com gráficos interativos (temperatura, umidade e precipitação).
- Implementar um sistema básico de autenticação de usuários.

## 3. Público-Alvo
- **Primário (Atual):** Avaliadores acadêmicos e professores da disciplina de estágio.
- **Secundário (Visão Futura):** Meteorologistas, estudantes e público geral interessado no histórico e previsão do tempo local.
- **Nível Técnico:** Leigo a intermediário (a interface deve ser intuitiva, sem exigir conhecimento técnico para interpretação dos gráficos).

## 4. Escopo Incluído (O que o sistema FAZ)
- **Localidade:** Cidade de Recife/PE (foco inicial).
- **Período de Dados:** 
  - Histórico: Último trimestre (aproximadamente 90 dias).
  - Previsão: Próximos 7 dias.
- **Variáveis Climáticas:** Temperatura (máxima, mínima e média), Umidade relativa do ar e Precipitação.
- **Funcionalidades:** Cadastro/Login de usuários, coleta automatizada ou sob demanda, cálculo de indicadores (ex: média do período, total de chuva) e visualização em dashboard.

## 5. Escopo Excluído (O que o sistema NÃO FAZ nesta versão)
- Suporte a múltiplas cidades (será uma funcionalidade de fases futuras).
- Envio de alertas meteorológicos em tempo real (push notifications ou e-mail).
- Desenvolvimento de aplicativo móvel nativo (Android/iOS).
- Integração com APIs que exigem burocracia de acesso ou pagamento (ex: INMET em sua forma mais complexa).
- Previsão climática de longo prazo (sazonal ou anual).

## 6. Requisitos Funcionais (RF)
- **RF01:** O sistema deve permitir o cadastro, login e logout de usuários.
- **RF02:** O sistema deve consumir a API Open-Meteo para obter dados históricos (90 dias) e de previsão (7 dias) de Recife.
- **RF03:** O sistema deve validar e armazenar os dados recebidos em um banco de dados PostgreSQL.
- **RF04:** O sistema deve calcular indicadores básicos, como média de temperatura e volume total de precipitação do período consultado.
- **RF05:** O sistema deve disponibilizar os dados através de uma API REST própria (Django REST Framework).
- **RF06:** O sistema deve exibir um dashboard web com gráficos interativos das variáveis climáticas ao longo do tempo.

## 7. Requisitos Não Funcionais (RNF)
- **RNF01 (Desempenho):** O dashboard deve carregar e renderizar os gráficos em menos de 3 segundos em uma conexão de banda larga padrão.
- **RNF02 (Usabilidade):** A interface do dashboard deve ser responsiva, adaptando-se razoavelmente a telas de dispositivos móveis, embora o foco de desenvolvimento seja a experiência em desktop.
- **RNF03 (Tecnologia):** O backend deve ser desenvolvido em Python (Django + Django REST Framework), o banco de dados em PostgreSQL e o frontend com HTML, CSS, JavaScript e uma biblioteca de gráficos (ex: Chart.js).

## 8. Critérios de Aceitação
- O usuário consegue se cadastrar e acessar o dashboard protegido.
- Ao acessar o dashboard, os gráficos exibem dados reais dos últimos 90 dias e dos próximos 7 dias sem erros de carregamento.
- O banco de dados contém registros com as colunas: data, temperatura_max, temperatura_min, umidade e precipitação.

## 9. Limitações Conhecidas
- A precisão dos dados depende inteiramente da disponibilidade e da grade de estimativa da API Open-Meteo para a região de Recife.
- Em caso de indisponibilidade da API externa, o sistema exibirá apenas os dados históricos já armazenados no banco, sem atualizar a previsão.

## 10. Entregáveis
- Repositório GitHub com o código-fonte documentado.
- Documento de escopo e arquitetura do sistema.
- Aplicação web funcional rodando localmente (ou em ambiente de homologação).

## 11. Cronograma Macro (Etapas de Desenvolvimento)
1. Definição do escopo e ambiente.
2. Desenvolvimento do Pipeline ETL (Extração e Transformação).
3. Configuração do Banco de Dados (PostgreSQL) e Modelagem Django.
4. Desenvolvimento da API REST e lógica de indicadores.
5. Implementação do Frontend (Dashboard e Gráficos).
6. Autenticação, testes, documentação e finalização.