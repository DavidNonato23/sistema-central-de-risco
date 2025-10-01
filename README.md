# 🛡️ Sistema Central de Análise de Risco (SCAR)

## 🎯 Visão Geral do Projeto

O **Sistema Central de Análise de Risco (SCAR)** é um projeto de Data Analytics e Cibersegurança que demonstra a construção de um *pipeline* completo (Python + Power BI) para detecção e priorização de ameaças a partir de logs de acesso web simulados.

O principal objetivo é transformar dados de log brutos em Inteligência de Segurança acionável, permitindo a identificação imediata de IPs maliciosos, tentativas de intrusão (`401`, `403`) e a visualização da **Taxa de Falha** do sistema.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Bibliotecas de Dados:** Pandas (`pd`)
* **Visualização & BI:** Microsoft Power BI Desktop
* **Modelagem de Dados:** DAX (Data Analysis Expressions)

## 🔑 Módulos e Funcionalidades Chave

O projeto é dividido em um processo de 3 etapas:

### 1. Python: Extração e Enriquecimento de Risco (Módulo ETL)

O script Python (`sistema_analise_risco.py`) é responsável por:

* **Coleta Simulada:** Geração de logs de acesso (Status Code, DataHora, IP).
* **Risco de IP (Inteligência de Ameaças):** Verifica IPs contra uma **Lista Negra** simulada e adiciona a coluna booleana `IP_Risco`.
* **Classificação de Criticidade:** Adiciona a coluna `Criticidade` para categorizar o evento como **'ALERTA_ATENCAO'** (Status >= 400) ou **'SUCESSO_NORMAL'** (Status < 400).

### 2. Power BI: Modelagem e KPIs (Módulo DAX)

O Power BI conecta-se diretamente ao script Python e usa DAX para criar métricas analíticas:

* **KPI Principal:** Criação da medida **`Taxa de Falha`** (`Total de Alertas` / `Total de Logs`) para medir o nível de risco do sistema.
* **Medidas Base:** `Total de Logs` e `Total de Alertas`.

### 3. Dashboard: Visualização e Priorização

O dashboard final é desenhado para guiar a investigação de segurança:

* **Priorização:** **Gráfico de Rosca** mostrando a proporção de `ALERTA_ATENCAO` vs. `SUCESSO_NORMAL`.
* **Tendência:** **Gráfico de Linhas** para monitorar picos de alertas ao longo do tempo.
* **Rastreamento:** **Gráfico de Barras** para detalhar os tipos de falha (`401`, `403`, `500`) e uma **Tabela** para rastrear os IPs de origem suspeitos.

## ⚙️ Como Executar o Projeto

1.  **Pré-requisitos:** Instale Python, Pandas (`pip install pandas`) e o Power BI Desktop.
2.  **Preparação:** Salve o código Python (`sistema_analise_risco.py`).
3.  **Conexão no Power BI:**
    * No Power BI Desktop, vá em **Obter Dados > Script do Python**.
    * Cole todo o conteúdo do script Python.
    * Carregue a tabela **`df_mestre_logs`**.
4.  **Modelagem:** Crie as medidas DAX (`Total de Logs`, `Total de Alertas`, `Taxa de Falha`).
5.  **Visualização:** Monte os visuais conforme a estrutura de Priorização de Risco.

## ✨ Aprendizados e Demonstrações

Este projeto demonstra:

* Criação de um pipeline de ETL (Python) do zero.
* Habilidade em análise de dados de cibersegurança e risco.
* Proficiência em DAX para criar métricas de negócio a partir de dados técnicos.
* Criação de um dashboard interativo focado na priorização de problemas.
