from database.conexao import Conexao

def recuperar_musicas():
    # passo um e dois
    con, cur = Conexao.conectar()
    cur.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")
    musicas = cur.fetchall()
    con.close()

    return musicas

