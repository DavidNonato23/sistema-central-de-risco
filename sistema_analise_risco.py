import pandas as pd
import random
from datetime import datetime, timedelta
import os 

ips_comuns = ['192.168.1.107', '192.168.1.111', '10.0.0.5', '172.31.255.255']
ips_suspeitos = ['203.0.113.44', '198.51.100.12', '172.16.0.1', '1.1.1.1']
status_sucesso = [200, 302]
status_alerta = [401, 403, 500]

registros = []
hora_inicio = datetime.now() - timedelta(hours=1)

for i in range(200):
    
    if i < 150: 
        ip = random.choice(ips_suspeitos)  
        status = random.choice(status_alerta)  
        recurso = '/admin/config' 
        agente = 'curl/7.64.1'
        
    else:
        ip = random.choice(ips_comuns)
        status = random.choice(status_sucesso)
        recurso = '/index.html'
        agente = 'Mozilla/5.0'

    tempo = hora_inicio + timedelta(seconds=i*random.randint(1, 10), microseconds=i)
    
    registros.append({
        'IP_Origem': ip,
        'DataHora': tempo,
        'Status': status,
        'Recurso': recurso,
        'Agente': agente
    })

df_mestre_logs = pd.DataFrame(registros)

status_alertas_set = set(status_alerta)
df_mestre_logs['Criticidade'] = df_mestre_logs['Status'].apply(
    lambda x: 'ALERTA_ATENCAO' if x in status_alertas_set else 'SUCESSO_NORMAL'
)

ips_suspeitos_set = set(ips_suspeitos)
df_mestre_logs['IP_Risco'] = df_mestre_logs['IP_Origem'].apply(
    lambda x: 'SIM' if x in ips_suspeitos_set else 'NÃO'
)

diretorio_saida = 'output'
if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)

caminho_arquivo = os.path.join(diretorio_saida, 'dados_scar.csv')
df_mestre_logs.to_csv(caminho_arquivo, index=False, encoding='utf-8')

print(f"Arquivo de logs de segurança gerado com sucesso em: {caminho_arquivo}")
print(f"Total de Registros Gerados: {len(df_mestre_logs)}")