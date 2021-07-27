import sqlite3
from sqlite3 import Error


def contectar_banco():
    caminho = '/home/valdomiro/Documentos/sqlite_dfbcursos/agenda.db'
    conect = None
    try:
        conect = sqlite3.connect(caminho)
        print('Conectado')
    except Error as ex:
        print(ex, '--Não conectou')
    return conect


conectar = contectar_banco()


def criar_cursor(conect):
    cur = None
    try:
        cur = conect.cursor()
        print('Cursor criado')
    except Error as exx:
        print(exx, '--Cursor não criado')
    return cur


cursor = criar_cursor(conectar)


def mostrar(cur):
    cursor.execute(f"SELECT * FROM {cur}")
    cosult = cursor.fetchall()
    return cosult


consulta = mostrar('tb_contatos')

for i in consulta:
    print(i)

conectar.close()
