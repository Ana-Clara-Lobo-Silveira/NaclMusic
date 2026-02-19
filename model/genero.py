from database.conexao import Conexao

def recuperar_generos():
    con, cur  = Conexao.conectar()
    cur.execute("SELECT nome_genero, icone, cor FROM genero;")
    generos = cur.fetchall()
    con.close()

    return generos