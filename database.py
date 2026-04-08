import sqlite3
import shutil
import os
from datetime import datetime

# -------------------------
# CONEXÃO
# -------------------------
def conectar():
    return sqlite3.connect("empresa.db", check_same_thread=False)

# -------------------------
# LOG DE ERROS
# -------------------------
def log_erro(erro):
    with open("erros.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {str(erro)}\n")

# -------------------------
# BACKUP
# -------------------------
def fazer_backup():
    if os.path.exists("empresa.db"):
        os.makedirs("backup", exist_ok=True)
        data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        destino = f"backup/empresa_backup_{data}.db"
        shutil.copy("empresa.db", destino)

# -------------------------
# CRIAR TABELA
# -------------------------
def criar_tabela():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cargo TEXT,
            salario REAL
        )
        """)

        conn.commit()
        conn.close()
    except Exception as e:
        log_erro(e)

# -------------------------
# ADICIONAR
# -------------------------
def adicionar(nome, cargo, salario):
    try:
        fazer_backup()

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)",
            (nome, cargo, salario)
        )

        conn.commit()
        conn.close()

        return True
    except Exception as e:
        log_erro(e)
        return False

# -------------------------
# LISTAR
# -------------------------
def listar():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM funcionarios")
        dados = cursor.fetchall()

        conn.close()
        return dados
    except Exception as e:
        log_erro(e)
        return []

# -------------------------
# DELETAR
# -------------------------
def deletar(id):
    try:
        fazer_backup()

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id,))

        conn.commit()
        conn.close()

        return True
    except Exception as e:
        log_erro(e)
        return False

# -------------------------
# ATUALIZAR
# -------------------------
def atualizar(id, nome, cargo, salario):
    try:
        fazer_backup()

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE funcionarios
        SET nome = ?, cargo = ?, salario = ?
        WHERE id = ?
        """, (nome, cargo, salario, id))

        conn.commit()
        conn.close()

        return True
    except Exception as e:
        log_erro(e)
        return False