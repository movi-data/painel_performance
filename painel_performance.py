import pandas as pd

# --- ETAPA 1: Carregar o arquivo ---
df_propostas = pd.read_csv("propostas.csv", sep=";", encoding="utf-8", low_memory=False)

# --- ETAPA 2: Preparar Colunas ---

# Tranformar 'Canal' em maiuscula
df_propostas['Canal'] = df_propostas['Canal'].str.upper()
# Filtrar o primeiro Canal na coluna 'Canal'
df_propostas['Canal'] = df_propostas['Canal'].str.split(',').str[0]

# Trocar na coluna 'Origem' onde for 'MobiBot' por 'Internet'
df_propostas['Origem'] = df_propostas['Origem'].replace('MobiBot', 'Internet')

# Filtrar leads apenas com 'Internet' em 'Origem'
df_propostas = df_propostas[df_propostas['Origem'] == 'Internet']

# --- ETAPA 3: Fazer agrupamento ---

# Agrupar leads por mês na coluna 'Data' e 'Canal'
leads_por_canal_mes = df_propostas.groupby([pd.to_datetime(df_propostas["Data"], format="%d/%m/%Y", errors='coerce').dt.to_period("d"),
                                            "Canal"]).size().reset_index(name="Quantidade de Leads")

# --- ETAPA 4: Criar arquivo csv e download ---

# Criar arquivo .csv
leads_por_canal_mes.to_csv("leads_por_canal_mes.csv",sep=";" ,index=False)

# Visualização para conferência no console
print(leads_por_canal_mes.head())
