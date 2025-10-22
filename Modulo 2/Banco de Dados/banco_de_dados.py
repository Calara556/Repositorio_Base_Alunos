import sqlite3

con = sqlite3.connect("Meu_banco.db")

try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor()

    #cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")

    #cur.execute("INSERT INTO pessoa VALUES(1, 'Maria Clara', 15, 'XXX.XXX.XXX-XX')")

    cur.execute("DELETE FROM  pessoa WHERE id = 1")

    '''res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchone()

    print(pessoas)
    cur.close()'''

    con.commit()

except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')
