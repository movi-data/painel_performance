import pandas as pd

# --- ETAPA 1: Carregar o arquivo ---
df_propostas = pd.read_csv("propostas.csv", sep=";", encoding="utf-8", low_memory=False)

df_canal = df_propostas.copy()

# --- ETAPA 2: Transforar Colunas ---

# Tranformar 'Canal' em maiuscula
df_canal['Canal'] = df_canal['Canal'].str.upper()
# Filtrar o primeiro Canal na coluna 'Canal'
df_canal['Canal'] = df_canal['Canal'].str.split(',').str[0]

# Trocar na coluna 'Origem' onde for 'MobiBot' por 'Internet'
df_canal['Origem'] = df_canal['Origem'].replace('MobiBot', 'Internet')

# Trocar na coluna 'Origem' onde for 'MobiBot' por 'Internet'
df_canal['Origem'] = df_canal['Origem'].replace('MobiBot', 'Internet')

# Renomear coluna 'qualificado'
df_canal.rename(columns={'qualificado': 'Qualificado'}, inplace=True)

# --- ETAPA 3: Fazer agrupamento ---

# Agrupar leads por mês na coluna 'Data' , 'Canal' e 'Qualificado'

leads_por_canal_mes = df_canal.groupby([pd.to_datetime(df_canal["Data"], format="%d/%m/%Y", errors='coerce').dt.to_period("d"),
                                            "Canal","Qualificado"]).size().reset_index(name="Quantidade de Leads")

# --- ETAPA 4: Criar arquivo csv e download ---

# Criar arquivo .csv
leads_por_canal_mes.to_csv("leads_por_canal_mes.csv",sep=";" ,index=False)

# Visualização para conferência no console
print(leads_por_canal_mes.tail())
