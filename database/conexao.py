import mysql.connector

class Conexao():

    # transforma em metodo estático, só precisa chama-lo
    @staticmethod
    def conectar():
        tipo_local = "nuvem"
        if tipo_local == "local":
            con = mysql.connector.connect(
                host="localhost",
                port = 3306,
                user = "root",
                password="root",
                database = "naclmusic"
            )
            cur = con.cursor(dictionary=True)
        else:
            con = mysql.connector.connect(
                host="localhoserver-nacl-nacl-music.a.aivencloud.comst",
                port = 23340,
                user = "avnadmin",
                password="AVNS_2VJEs0HZhnTymSnnDJj",
                database = "naclmusic"
            )
            cur = con.cursor(dictionary=True)

        return con, cur