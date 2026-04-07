import pandas as pd

# -------------------------
# FORMATAÇÃO
# -------------------------

def formatar_salario(valor):
    try:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "R$ 0,00"

# -------------------------
# CÁLCULOS
# -------------------------

def calcular_media(df):
    if not df.empty:
        return df["Salario"].mean()
    return 0

def calcular_total(df):
    return len(df)

def maior_salario(df):
    if not df.empty:
        return df["Salario"].max()
    return 0

# -------------------------
# FILTROS
# -------------------------

def filtrar_nome(df, nome):
    if nome:
        return df[df["Nome"].str.contains(nome, case=False)]
    return df

# -------------------------
# VALIDAÇÃO
# -------------------------

def validar_campos(nome, cargo, salario):
    if not nome or not cargo:
        return False, "Nome e cargo são obrigatórios"
    
    if salario < 0:
        return False, "Salário inválido"
    
    return True, "OK"

# -------------------------
# CONVERSÃO
# -------------------------

def lista_para_dataframe(dados):
    return pd.DataFrame(dados, columns=["ID", "Nome", "Cargo", "Salario"])