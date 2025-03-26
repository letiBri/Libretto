import mysql.connector


class DBConnect:
    @classmethod #decoratore che mi dice che questo metodo è un metodo di classe ed è unico
    # indica che questa classe è unica
    def getConnection(self):
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

