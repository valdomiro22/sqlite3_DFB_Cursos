import sqlite3
from sqlite3 import Error


def conexao_banco():
    caminho_banco = '/home/valdomiro/Documentos/sqlite_dfbcursos/agenda.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho_banco)
        print('Conexão bem sucedida')
    except Error as ex:
        print(ex, 'Conexão mal sucedida')
    return conexao


comando_sql = """CREATE TABLE tb_contatos2 (
                id_contato INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_contato VARCHAR(30),
                telefone_contato VARCHAR(14),
                email_contato VARCHAR(30)
            );"""


# O cursor será criado aqui
def cria_cursor(conect):
    cur = None
    try:
        cur = conect.cursor()
        print('Cursor criado')
    except Error as ex:
        print(ex, '--Cursor não foi criado')
    return cur


cursor = cria_cursor(conexao_banco())


# def criar_tabela(curs, comand):
#     try:
#         curs.execute(comand)
#         print('Tabela criada')
#     except Error as ex:
#         print(ex, '---Tabela não foi criada')
#
#
# criar_tabela(cursor, comando_sql)


# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
# cursor.execute("INSERT INTO pessoas VALUES ('Maria', 30, 'maria@gmail.com')")

# banco.commit()


def mostrar(item):
    cursor.execute(f"SELECT * FROM {item}")
    print(cursor.fetchall())


mostrar('tb_contatos')
mostrar('tb_contatos2')
