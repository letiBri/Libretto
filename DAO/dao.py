import mysql.connector

from DAO.DBConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:
    #def __init__(self):
        #self.dbConnect = DBConnect()

    def getAllVoti(self):
        cnx = DBConnect.getConnection() # al posto di scrivere le info qui chiamo il metodo nel dbConnect che è un classmehof
        cursor = cnx.cursor(dictionary=True)

        query = """select * from voti"""
        cursor.execute(query)

        res = []
        for row in cursor:
            materia = row["materia"]
            punteggio = row["punteggio"]
            lode = row["lode"]
            data = row["data"].date() #string python sa gia fare la conversione da varchar a string
            if lode == "False":
                res.append(Voto(materia, punteggio, data, False))
            else:
                res.append(Voto(materia, punteggio, data, True))

        cnx.close()
        return res


    def addVoto(self, voto):
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = ("insert into voti (materia, punteggio, data, lode) "
                 "values(%s, %s, %s, %s)")
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit() #meotodo della connessione quando modifico il database
        cnx.close()
        return


    def hasVoto(self, voto: Voto):
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor()
        query = """select * from voti v where v.materia = %s """ #provo la query su dbeaver
        cursor.execute(query, (voto.materia, ))
        res = cursor.fetchall() #lista di righe che in questo caso saranno 0 o 1
        cnx.close()
        return len(res) > 0 #se è maggiore di zero vuol dire che quel voto c'è nel database


if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()
