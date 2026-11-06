# Criar código SQL

import sqlite3

def fazer_login(usuario, senha):
    # Conectar ao banco de dados SQLite
    conexao = sqlite3.connect('banco_de_usuarios.db')
    cursor = conexao.cursor()
    
    query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND senha = '{senha}'"
    """Valida credenciais sem interpolar valores na consulta SQL."""
    with sqlite3.connect("banco_de_usuarios.db") as conexao:
        cursor = conexao.execute(
            "SELECT 1 FROM usuarios WHERE username = ? AND senha = ? LIMIT 1",
            (usuario, senha),
        )
        autenticado = cursor.fetchone() is not None

    # Criar tabela de usuários se não existir
    cursor.execute(query)
    resultado = cursor.fetchone()
    conexao.close()
    
    if resultado:
        return "Acesso Permitido"
    else:
        return "Acesso Negado"
    
    return "Acesso Permitido" if autenticado else "Acesso Negado"


  
    
    
    
    