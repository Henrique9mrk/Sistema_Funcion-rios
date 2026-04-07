import streamlit as st
import pandas as pd
from database import *
from utils import *

st.set_page_config(layout="wide")

criar_tabela()

st.title("📊 Sistema de Funcionários")

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Cadastrar"])

dados = listar()
df = pd.DataFrame(dados, columns=["ID", "Nome", "Cargo", "Salario"])

# -------------------------
# DASHBOARD
# -------------------------
if menu == "Dashboard":

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Funcionários", len(df))

    with col2:
        if not df.empty:
            st.metric("Média Salarial", f"R$ {df['Salario'].mean():.2f}")

    busca = st.text_input("Buscar funcionário")

    if busca:
        df = df[df["Nome"].str.contains(busca, case=False)]

    st.dataframe(df, use_container_width=True)

    st.subheader("Remover funcionário")

    if not df.empty:
        id_selecionado = st.selectbox("Selecione ID", df["ID"])

        if st.button("Excluir"):
            deletar(id_selecionado)
            st.success("Removido com sucesso!")

# -------------------------
# CADASTRO
# -------------------------
elif menu == "Cadastrar":

    st.subheader("Novo Funcionário")

    nome = st.text_input("Nome")
    cargo = st.text_input("Cargo")
    salario = st.number_input("Salário", min_value=0.0)

    if st.button("Salvar"):
        if nome and cargo:
            adicionar(nome, cargo, salario)
            st.success("Funcionário cadastrado!")
        else:
            st.warning("Preencha todos os campos")