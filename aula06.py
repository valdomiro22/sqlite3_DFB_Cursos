import os
import sqlite3
from sqlite3 import Error


def criar_conexao():
    caminho = '/home/valdomiro/Documentos/sqlite_dfbcursos/agenda.db'
    conec = None
    try:
        conec = sqlite3.connect(caminho)
        print('Conectado')
    except Error as ex:
        print(ex, "Não conectou")
    return conec


conectar = criar_conexao()


def criar_cursor(con):
    cur = None
    try:
        cur = con.cursor()
        print('Criou cursor')
    except Error as exx:
        print(exx, 'Não criou cursor')
    return cur


cursor = criar_cursor(conectar)


def executar_acoes(conec, comand):
    ac = None
    try:
        ac = conec.cursor()
        ac.execute(comand)
        conec.commit()
        print('Ação executada')
    except Error as err:
        print(err, '--Ação não executada')
    return ac


def mostrar(tabel):
    cursor.execute(f"""SELECT * FROM {tabel};""")
    cons = cursor.fetchall()
    return cons


imprimir = mostrar('bicicleta')
for i in imprimir:
    print(i)

acao = int(input('Escolha a ação que deseja executar\n'
                 '[0] - Sair\n'
                 '[1] - Criar tabela\n'
                 '[2] - Adicionar elemento\n'
                 '[3] - Deletar campo\n'
                 '[4] - Atualizar informação\n'
                 'Ação: '))

comando = None

if acao < 0 or acao > 4:
    print('Ação invalida')
elif acao == 0:
    print('Saindo sem executar nenhuma ação\n')
else:
    if acao == 1:
        nome_tabela = input('Informe o nome da tabela: ')
        informacoes_tabela = input('Digite as informações da tabela (id ja esta criado): ')

        comando = f"""CREATE TABLE {nome_tabela} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {informacoes_tabela}
                );"""
    elif acao == 2:
        marca = input('Marca: ')
        uso = input('Uso: ')
        aro = input('Aro: ')

        comando = f"""INSERT INTO bicicleta 
                            (marca, uso, aro)
                            VALUES ('{marca}', '{uso}', '{aro}')
                        ;"""
    elif acao == 3:
        ident = input('id: ')
        comando = f"""DELETE FROM bicicleta WHERE id = {ident};"""
    elif acao == 4:
        campo = input('Campo que deseja atualizar'
                      '[marca] [uso] [aro]: ')
        valor = input('Valor que deseja setar: ')
        identif = int(input('id do elemento: '))

        comando = f"""UPDATE bicicleta SET {campo} = '{valor}' WHERE id = {identif};"""

    executar_acoes(conectar, comando)

most = mostrar('bicicleta')
print()
for i in most:
    print(i)

conectar.close()
