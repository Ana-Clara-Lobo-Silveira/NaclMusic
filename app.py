from flask import Flask, render_template, redirect, request, session
from model.musica import recuperar_musicas, salvar_musica
from model.genero import recuperar_generos



app = Flask(__name__)

@app.route("/", methods = ["GET"])
def pg_principal():

    musicas = recuperar_musicas()
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





if __name__ == "__main__":
    app.run(debug=True)
