from database.conexao import Conexao

def cadastro(usuario:str, senha:str):
    try:
        con, cur  = Conexao.conectar()
        cur.execute("INSERT INTO cadastro (usuario,senha) VALUES (%s, %s)", [usuario, senha])
        con.commit()
        con.close()

        return True
    except Exception as erro:
        print(erro)
        return False
    
