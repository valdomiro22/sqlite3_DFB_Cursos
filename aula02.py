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


vcom = conexao_banco()

# nome = input('Digite o nome: ')
# telefone = input("Digite o telefone: ")
# email = input("Digite o email: ")

# comando_sql = f"""INSERT INTO tb_contatos
#                 (nome_contato, telefone_contato, email_contato)
#                 VALUES ('{nome}', '{telefone}', '{email}')
#                 ;"""


def cria_cursor(conect):
    cur = None
    try:
        cur = conect.cursor()
        print('Cursor criado')
    except Error as exx:
        print(exx, '--Cursor não foi criado')
    return cur


cursor = cria_cursor(conexao_banco())


# def inserir(co, comand):
#     try:
#         c = co.cursor()
#         c.execute(comand)
#         print('Dados inseridos')
#         co.commit()
#     except Error as ex:
#         print(ex, '---Dados não inseridos')


# inserir(vcom, comando_sql)
# vcom.commit()


def mostrar(item):
    cursor.execute(f"SELECT * FROM {item}")
    print(cursor.fetchall())


mostrar('tb_contatos')
conexao_banco().close()
