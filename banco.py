import os
import sqlite3
import sys

def pasta_do_programa():
    '''Descobre a pasta onde o programa esta'''
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(pasta_do_programa(),'alunos.db')

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def criar_tabela():
    '''Cria a tabela de alunos se ela ainda não existir'''
    conn = conectar()
    conn.execute('''
      CREATE TABLE IF NOT EXISTS alunos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      nota1 REAL NOT NULL,
      nota2 REAL NOT NULL
      )
''')
    conn.commit()
    conn.close()

def inserir_alunos():
    '''Devolve uma lista de tuplas: (id, nome, nota1, nota2)'''  
    conn = conectar()
    conn.execute(
        'INSERT INTO alunos (nome, nota1, nota2) VALUES (?, ?, ?)'
    )  
    conn.commit()
    conn.close()

def listar_alunos():
    conn = conectar()
    linhas = conn.execute(
        'SELECT id, nome, nota1, nota2 FROM alunos ORDER BY nome'
    ).fetchall()
    conn.close()
    return linhas

def buscar_por_nome(texto):
    '''Buscar aluno cujo nome contem o texto (ignora maiusculas)'''
    conn = conectar()
    linhas = conn.execute(
        'SELECT id, nome, nota1, nota2 FROM alunos WHERE nome LIKE  ? ORDER BY nome',
    )    