import mysql.connector


class LibrettoDAO:
    def getAllVoti(self):
        cnx = mysql.connector.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            database="libretto")
        cursor = cnx.cursor(dictionary=True)

        query = """select * from voti"""
        rs = cursor.execute(query)

        for row in cursor:
            print(row)
        cnx.close()

if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()
