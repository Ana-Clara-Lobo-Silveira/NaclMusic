from flask import Flask, render_template, redirect, request, session
from model.musica import recuperar_musicas, salvar_musica, excluir_musica, status_musica
from model.genero import recuperar_generos
from model.cadastro import cadastro
from model.cadastro import verifica_cadastrado





app = Flask(__name__)


@app.route("/", methods = ["GET"])
def pg_principal():

    musicas = recuperar_musicas(True)
    generos = recuperar_generos()
    return render_template("principal.html", musicas_html=musicas, genero_html = generos)

@app.route("/admin")
def pg_administracao():
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("administracao.html", musicas_html = musicas, genero_html = generos)


@app.route("/musica/post", methods=["POST"])
def api_ins_musica():
    nome = request.form.get("nome")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url_imagem = request.form.get("url_imagem")
    genero = request.form.get("genero")
    if salvar_musica(nome, cantor, duracao, url_imagem, genero):
        return redirect("/admin")
    else:
        return "Erro"

@app.route("/musica/delete/<codigo>")
def deletar_musica(codigo):
    excluir_musica(codigo)
    return redirect("/admin")

@app.route("/musica/ativar/<ativar>/<codigo>")
def ativar_musica(ativar, codigo):
    status_musica(ativar, codigo)
    return redirect("/admin")

@app.route("/cadastro", methods = ["GET"])
def pg_cadastro_get():
    return render_template("cadastro.html")

@app.route("/cadastro", methods = ["POST"])
def pg_cadastro():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if cadastro(usuario, senha):
        return redirect("/admin")
    else:
        return "Complete as informações corretamente"
    
@app.route("/login", methods = ["GET"])
def pg_login_get():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def pg_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if verifica_cadastrado(usuario,senha):
        return redirect("/admin")
    else:
        return "Complete as informações corretamente"

if __name__ == "__main__":
    app.run(debug=True)
