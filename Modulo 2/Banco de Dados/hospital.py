import sqlite3

try:
    con = sqlite3.connect('hospital.db')
    cur = con.cursor()

    cur.executescript("DELETE FROM paciente WHERE id = 37")

    cur.close()
    con.close()
except ConnectionRefusedError as e:
    print('Erro de conexão: ', e)