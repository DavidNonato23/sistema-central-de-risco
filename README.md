🛡️ Sistema Central de Análise de Risco (SCAR)
🎯 Visão Geral do Projeto
O Sistema Central de Análise de Risco (SCAR) é um projeto de Data Analytics e Cibersegurança que demonstra a construção de um pipeline completo (Python + Power BI) para detecção e priorização de ameaças a partir de logs de acesso web simulados.

O principal objetivo é transformar dados de log brutos em Inteligência de Segurança Acionável, permitindo a identificação imediata de IPs maliciosos e a visualização da Taxa de Falha do sistema.

🛠️ Tecnologias e Habilidades Chave

<img width="988" height="111" alt="image" src="https://github.com/user-attachments/assets/734f49e8-2cdc-4466-a207-43fa173a9e24" />


🔑 Módulos e Funcionalidades Chave
1. Python: Enriquecimento de Risco (Módulo ETL)
Classificação de Criticidade: Categoriza o evento como 'ALERTA_ATENCAO' (Status >= 400).

Inteligência de Ameaças: Adiciona a flag de risco (IP_Risco) verificando a origem contra uma Lista Negra simulada.

2. Solução de Engenharia: Estabilidade do Pipeline
O projeto implementou uma solução robusta para contornar falhas de conexão Python/Power BI:

O módulo os é utilizado para criar e exportar o CSV de forma estável, garantindo que o Power BI sempre acesse o novo lote de dados.

3. Power BI: Modelagem e Priorização
KPI Principal: Medida Taxa de Falha (Total de Alertas / Total de Logs) para medir o risco geral do sistema.

Rastreamento: A Tabela de Detalhamento permite rastrear o IP de Origem, o horário e o Recurso Acessado.

📊 Demonstração do Projeto em Ação
O projeto está configurado com um Simulador de Ataque Sustentado para testar a capacidade de detecção do sistema.

Simulação de Ataque Sustentado (Python)
O código Python gera 200 logs, dos quais 75% são forçados a ser alertas (i < 150), testando a estabilidade do pipeline e a capacidade de detecção do sistema em tempo real.

<img width="1920" height="1011" alt="Código Python Simulação de Ataque" src="https://github.com/user-attachments/assets/0bc0e82b-8118-4316-a742-2852c01b6137" />



<img width="1920" height="1007" alt="Captura de tela 2025-10-01 193107" src="https://github.com/user-attachments/assets/222ad2f6-e33f-4e99-bd09-4788da6cd8aa" />

Visão Geral e Priorização de Risco (Power BI)
O dashboard demonstra o salto no KPI, provando a detecção:

A Taxa de Falha salta para 75% após o ataque simulado.

O Gráfico de Rosca permite o filtro imediato dos eventos ALERTA_ATENCAO.

<img width="1596" height="805" alt="Visão Geral e KPIs" src="https://github.com/user-attachments/assets/7ff6c3e4-2c96-4b35-bc98-d7c04600fd3b" />

Rastreamento e Acionabilidade
A Tabela de Detalhamento é a ferramenta mais valiosa, transformando a visualização em ação. Ela permite rastrear o horário exato do ataque e os recursos que foram alvo da tentativa de invasão.

<img width="1920" height="1011" alt="Tabela de Rastreamento" src="https://github.com/user-attachments/assets/8030b365-c95f-4c02-ab36-d6642f745306" />

✨ Conclusão: Aprendizados e Habilidades
Este projeto demonstra a habilidade de:

Criar um pipeline de ETL em Python do zero e resolver problemas de infraestrutura.

Aplicar lógica de análise de risco e cibersegurança para enriquecimento de dados.

Desenvolver KPIs estratégicos em DAX a partir de dados técnicos.

Entregar um dashboard interativo e acionável, focado na priorização e resposta rápida a incidentes.priorização e resposta rápida a incidentes.
