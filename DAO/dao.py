import mysql.connector

from DAO.DBConnect import DBConnect
from voto.voto import Voto


class LibrettoDAO:
    #def __init__(self):
        #self.dbConnect = DBConnect()

    @staticmethod #dice che il metodo vede solo i parametri che gli passiamo come argomenti e non vede i parametri dell'istanza
    def getAllVoti():
        cnx = DBConnect.getConnection() #al posto di scrivere le info qui chiamo il metodo nel DBConnect che è un classmethod
        cursor = cnx.cursor(dictionary=True)

        query = """select * from voti"""
        cursor.execute(query)

        res = []
        for row in cursor:
            materia = row["materia"]
            punteggio = row["punteggio"]
            lode = row["lode"]
            data = row["data"].date() #string. Python sa già fare la conversione da varchar a string
            if lode == "False":
                res.append(Voto(materia, punteggio, data, False))
            else:
                res.append(Voto(materia, punteggio, data, True))

        cnx.close()
        return res

    @staticmethod
    def addVoto(voto):
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)
        query = ("insert into voti (materia, punteggio, data, lode) "
                 "values(%s, %s, %s, %s)")
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit() #meotodo della connessione quando modifico il database
        cnx.close()
        return

    @staticmethod
    def hasVoto(voto: Voto):
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor()
        query = """select * from voti v where v.materia = %s """ #provo la query su dbeaver quando sono più complicate
        cursor.execute(query, (voto.materia, )) #inserisco la tupla con un solo valore ma ricordarsi la virgola e lascio vuoto dopo
        res = cursor.fetchall() #lista di righe che in questo caso saranno 0 o 1
        cnx.close()
        return len(res) > 0 #se è maggiore di zero vuol dire che quel voto c'è nel database


if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()
