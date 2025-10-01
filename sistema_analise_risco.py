import pandas as pd
import random
from datetime import datetime, timedelta
import os 


ips_comuns = ['192.168.1.10', '192.168.1.11']
ips_suspeitos = ['203.0.113.44', '198.51.100.12']
status_sucesso = [200, 302]
status_alerta = [401, 403, 500]

registros = []
hora_inicio = datetime.now() - timedelta(hours=1)

for i in range(20):
    if random.random() < 0.3:
        ip = random.choice(ips_suspeitos)
        status = random.choice(status_alerta)
        recurso = '/admin/config'
        agente = 'curl/7.64.1'
    else:
        ip = random.choice(ips_comuns)
        status = random.choice(status_sucesso)
        recurso = '/index.html'
        agente = 'Mozilla/5.0'
    
    tempo = hora_inicio + timedelta(seconds=i * random.randint(10, 60))
    
    registros.append({
        'DataHora': tempo,
        'IP_Origem': ip,
        'Status': status,
        'Recurso': recurso,
        'UserAgent': agente
    })

df_bruto = pd.DataFrame(registros)


lista_negra = ['198.51.100.12', '10.10.10.10']

df_bruto['IP_Risco'] = df_bruto['IP_Origem'].apply(
    lambda x: 'SIM' if x in lista_negra else 'NÃO'
)

def checar_criticidade(status):
    if status >= 400:
        return 'ALERTA_ATENCAO'
    else:
        return 'SUCESSO_NORMAL'

df_bruto['Criticidade'] = df_bruto['Status'].apply(checar_criticidade)

df_bruto['UA_Suspeito'] = df_bruto['UserAgent'].apply(
    lambda x: 'SIM' if 'curl' in x or 'bot' in x else 'NÃO'
)

df_bruto['Recurso'] = df_bruto['Recurso'].str.lower()
df_bruto = df_bruto.drop(columns=['UserAgent'])

df_mestre_logs = df_bruto




NOME_DO_ARQUIVO = 'output/dados_scar.csv'


output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


df_mestre_logs.to_csv(NOME_DO_ARQUIVO, index=False, encoding='utf-8')