import streamlit as st
from database import *
from utils import *

st.set_page_config(page_title="Sistema de Funcionários", layout="wide")

# Inicialização
criar_tabela()

st.title("📊 Sistema de Funcionários")

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Cadastrar", "Editar"])

dados = listar()
df = lista_para_dataframe(dados)

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":

    # Métricas
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de Funcionários", calcular_total(df))

    with col2:
        st.metric("Média Salarial", formatar_salario(calcular_media(df)))

    with col3:
        st.metric("Maior Salário", formatar_salario(maior_salario(df)))

    # Busca
    busca = st.text_input("🔍 Buscar funcionário")
    df_filtrado = filtrar_nome(df, busca)

    # Tabela
    st.dataframe(df_filtrado, use_container_width=True)

    # Remoção
    st.subheader("🗑️ Remover funcionário")

    if not df_filtrado.empty:
        id_sel = st.selectbox("Selecione o ID", df_filtrado["ID"])

        if st.button("Excluir"):
            sucesso = deletar(id_sel)

            if sucesso:
                st.success("Funcionário removido!")
                st.rerun()
            else:
                st.error("Erro ao excluir funcionário.")
    else:
        st.info("Nenhum funcionário encontrado.")

# =========================
# CADASTRO
# =========================
elif menu == "Cadastrar":

    st.subheader("➕ Novo Funcionário")

    nome = st.text_input("Nome")
    cargo = st.text_input("Cargo")
    salario = st.number_input("Salário", min_value=0.0)

    if st.button("Salvar"):
        valido, msg = validar_campos(nome, cargo, salario)

        if not valido:
            st.warning(msg)
        else:
            sucesso = adicionar(nome, cargo, salario)

            if sucesso:
                st.success("Cadastrado com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao cadastrar.")

# =========================
# EDIÇÃO
# =========================
elif menu == "Editar":

    st.subheader("✏️ Editar Funcionário")

    if not df.empty:
        id_sel = st.selectbox("Selecione o ID", df["ID"])
        funcionario = df[df["ID"] == id_sel].iloc[0]

        nome = st.text_input("Nome", funcionario["Nome"])
        cargo = st.text_input("Cargo", funcionario["Cargo"])
        salario = st.number_input("Salário", value=float(funcionario["Salario"]))

        if st.button("Atualizar"):
            sucesso = atualizar(id_sel, nome, cargo, salario)

            if sucesso:
                st.success("Atualizado com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao atualizar.")
    else:
        st.info("Nenhum funcionário cadastrado.")