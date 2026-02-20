from database.conexao import Conexao

def recuperar_musicas():
    # passo um e dois
    con, cur = Conexao.conectar()
    cur.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")
    musicas = cur.fetchall()
    con.close()

    return musicas

def salvar_musica(nome: str, cantor: str, duracao: str, url_imagem: str, genero: str) -> bool:
    """
    Função capta os valores, salva e retorna boleano (verdadeiro ou falso).
    """

    try:
        con, cur = Conexao.conectar()
        cur.execute("INSERT INTO musica (nome, cantor, duracao, url_imagem, nome_genero) VALUES (%s,%s, %s, %s, %s)", [nome, cantor, duracao, url_imagem, genero] )
        con.commit()
        con.close()

        return True
    except:
        return False