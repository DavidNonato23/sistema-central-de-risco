🛡️ Sistema Central de Análise de Risco (SCAR)
🎯 Visão Geral do Projeto
O Sistema Central de Análise de Risco (SCAR) é um projeto de Data Analytics e Cibersegurança que demonstra a construção de um pipeline completo (Python + Power BI) para detecção e priorização de ameaças a partir de logs de acesso web simulados.

O principal objetivo é transformar dados de log brutos em Inteligência de Segurança Acionável, permitindo a identificação imediata de IPs maliciosos e a visualização da Taxa de Falha do sistema.

🛠️ Tecnologias e Habilidades Chave

<img width="988" height="111" alt="image" src="https://github.com/user-attachments/assets/734f49e8-2cdc-4466-a207-43fa173a9e24" />


🔑 Módulos e Funcionalidades Chave
1. Python: Enriquecimento de Risco (Módulo ETL)
O script Python (sistema_analise_risco.py) é responsável pelo core da inteligência:

Classificação de Criticidade: Categoriza o evento como 'ALERTA_ATENCAO' (Status >= 400) ou 'SUCESSO_NORMAL' (Status < 400).

Inteligência de Ameaças: Adiciona a flag de risco (IP_Risco) verificando a origem contra uma Lista Negra simulada.

2. Power BI: Modelagem e KPIs (Módulo DAX)
KPI Principal: Criação da medida Taxa de Falha (Total de Alertas / Total de Logs) para medir o nível de risco do sistema.

3. Solução de Engenharia: Estabilidade do Pipeline
O projeto foi configurado para resolver falhas comuns de conexão e permissão:

O pipeline utiliza o módulo os para criar e exportar o CSV de forma estável, garantindo que o Power BI sempre tenha acesso à fonte de dados, independente das configurações de ambiente.

📊 Demonstração do Projeto em Ação
O projeto está configurado com um Simulador de Ataque Sustentado (cerca de 200 logs gerados, com 75% classificados como alerta) para testar a capacidade de detecção do sistema em tempo real.

Visão Geral e Priorização de Risco
O dashboard fornece os KPIs de alto nível e permite a priorização imediata:

É possível monitorar o Dia, Mês e Ano da atividade.

O Gráfico de Rosca permite o filtro imediato dos alertas.

<img width="1596" height="805" alt="Visão Geral e KPIs" src="https://github.com/user-attachments/assets/7ff6c3e4-2c96-4b35-bc98-d7c04600fd3b" />

Rastreamento de Ameaças (Acionabilidade)
A Tabela de Detalhamento é a ferramenta mais valiosa para o analista, transformando a visualização em ação:

Detalhes do Incidente: Permite rastrear o horário exato do ataque, a origem do IP e os recursos específicos que foram alvo da tentativa de invasão (ex: /admin/config).

<img width="1920" height="1011" alt="Tabela de Rastreamento" src="https://github.com/user-attachments/assets/8030b365-c95f-4c02-ab36-d6642f745306" />

✨ Conclusão: Aprendizados e Habilidades
Este projeto demonstra a habilidade de:

Criar um pipeline de ETL em Python do zero.

Aplicar lógica de análise de risco e cibersegurança para enriquecimento de dados.

Desenvolver KPIs estratégicos em DAX a partir de dados técnicos.

Entregar um dashboard interativo e acionável, focado na priorização e resposta rápida a incidentes.
