import sqlite3
from sqlite3 import Error


def conexao_bando():
    caminho = '/home/valdomiro/Documentos/sqlite_dfbcursos/agenda.db'
    conect = None
    try:
        conect = sqlite3.connect(caminho)
        print('Conectado')
    except Error as ex:
        print(ex, '--Não ouve conexão')
    return conect


conectar = conexao_bando()


def criar_cursor(con):
    cur = None
    try:
        cur = con.cursor()
        print('Cursor criado')
    except Error as exx:
        print('Cursor não criado')
    return cur


cursor = criar_cursor(conectar)


def mostrar(it):
    cursor.execute(f"SELECT * FROM {it}")
    print(cursor.fetchall())


mostrar('tb_contatos')

campo = input('Qual campo deseja atualizar: ')
valor = input('Para qual valor deseja atualizar? ')
identificador = int(input('ID de destino: '))

# Se quiser alterar mais de um campo, é só colocar virgula e as informações referentes ao outro campo
comando_sql = f"""UPDATE tb_contatos SET {campo} = '{valor}' WHERE id_contato = {identificador};
                """


def atualizar(con, comand):
    try:
        a = con.cursor()
        a.execute(comand)
        con.commit()
    except Error as err:
        print(err, '--Atualizações não feitas')

        # def deletar(con, comand):
        #     try:
        #         c = con.cursor()
        #         c.execute(comand)
        #         con.commit()
        #         print('Dados apagados')
        #     except Error as err:
        #         print(err, '--Dados não apagador')


atualizar(conectar, comando_sql)

mostrar('tb_contatos')
conectar.close()
