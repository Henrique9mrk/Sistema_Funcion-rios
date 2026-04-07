import sqlite3

def conectar():
    return sqlite3.connect("empresa.db", check_same_thread=False)

def criar_tabela():
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

def adicionar(nome, cargo, salario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)",
        (nome, cargo, salario)
    )

    conn.commit()
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    dados = cursor.fetchall()

    conn.close()
    return dados

def deletar(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def atualizar(id, nome, cargo, salario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE funcionarios
    SET nome = ?, cargo = ?, salario = ?
    WHERE id = ?
    """, (nome, cargo, salario, id))

    conn.commit()
    conn.close()