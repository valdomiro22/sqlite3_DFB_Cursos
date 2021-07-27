import sqlite3
from sqlite3 import Error


def conexao_bando():
    caminho_banco = '/home/valdomiro/Documentos/sqlite_dfbcursos/agenda.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho_banco)
        print('Conexão bem sucedida')
    except Error as ex:
        print(ex, '--Conexão mal sucedida')
    return conexao


conectar = conexao_bando()


def mostrar(item):
    cursor.execute(f"SELECT * FROM {item}")
    print(cursor.fetchall())


def cria_cursor(conect):
    cur = None
    try:
        cur = conect.cursor()
        print('Cursor criado')
    except Error as exx:
        print(exx, '--Cursor não criado')
    return cur


cursor = cria_cursor(conectar)

mostrar('tb_contatos')
apagar = input('Informe o item que deseja deletar: ')

comando_sql = f""" DELETE FROM tb_contatos WHERE id_contato = {apagar}; """


def deletar(con, comand):
    try:
        c = con.cursor()
        c.execute(comand)
        con.commit()
        print('Dados apagados')
    except Error as err:
        print(err, '--Dados não apagador')


deletar(conectar, comando_sql)

mostrar('tb_contatos')

conexao_bando().close()
