from database.conexao import Conexao

def recuperar_musicas(ativos:bool=False):
    # passo um e dois
    con, cur = Conexao.conectar()
    
    if ativos == False:
        cur.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica;")
    else:
        cur.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica  WHERE ativo = 1;")
    
    
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
    except Exception as erro:
        print(erro)
        return False
    
def excluir_musica(codigo: int):
        con, cur = Conexao.conectar()
        cur.execute("DELETE FROM musica WHERE codigo = %s", [codigo] )
        con.commit()
        con.close()

def status_musica(ativo:bool,codigo:int):
        con, cur = Conexao.conectar()
        cur.execute("UPDATE musica SET ativo = %s WHERE codigo = %s", [ativo, codigo] )
        con.commit()
        con.close()