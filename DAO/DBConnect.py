import pathlib

import mysql.connector


class DBConnect:
    '''
    @classmethod #decoratore che mi dice che questo metodo è un metodo di classe ed è unico
    # indica che questa classe è unica
    def getConnection(cls): #metodo di classe prende come argomento la classe
        #crea una connessione e la ritorna oppure stampa l'errore
        try:
            cnx = mysql.connector.connect(user="root",
                password="root",
                host="127.0.0.1",
                database="libretto")
            return cnx

        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al database")
            print(err)
            return None
    '''

    def __init__(self):
        RuntimeError("Non creare un'istanza di questa classe per favore!")

    _myPool = None
    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            #creo una nuova connessione e restituisco il metodo get_connection
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(pool_size=3, pool_name="myPool",
                                                                          option_files=f"{pathlib.Path(__file__).resolve().parent}/connection.cfg") #risalgo al file che ha salvato tutte le info di host, psw ecc
            except mysql.connector.Error as err:
                print("Something is wrong in dbconnect")
                print(err)
                return None
            return cls._myPool.get_connection()
        else:
            # se il pool già esiste, restituisco direttamente la connessione
            return cls._myPool.get_connection()


