from flask import Flask, render_template, redirect, request, session
from musica import recuperar_musicas
from genero import recuperar_generos
import mysql.connector

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def pg_principal():

    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("principal.html", musicas_html=musicas, genero_html = generos)

@app.route("/admin")
def pg_administracao():
    musicas = recuperar_musicas()
    return render_template("administracao.html", musicas_html = musicas)





if __name__ == "__main__":
    app.run(debug=True)