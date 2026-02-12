from flask import Flask, render_template, redirect, request, session
import mysql.connector

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def pg_principal():

    #conectando bd
    con = mysql.connector.connect(
        host="localhost",
        port = 3306,
        user = "root",
        password="root",
        database = "NaclMusic"
    )
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")
    musicas = cur.fetchall()
    con.close()


    return render_template("principal.html", musicas_html=musicas)

# @app.route("/admin")
# def pg_administracao():
#     return render_template("administracao.html")





if __name__ == "__main__":
    app.run(debug=True)