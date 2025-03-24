import mysql


class LibrettoDAO:
    def getAllVoti(self):
        cnx = mysql.connector.Connection(
            user="root",
            password="rootroot",
            host="127.0.0.1",
            database="libretto")
        cursor = cnx.cursor(dictonary=True)

        query = """select * from voti"""
        rs = cursor.execute(query)

        for row in rs:
            print(row)
        cnx.close()

if __name__ == "__main__":
    mydao = LibrettoDAO()
    mydao.getAllVoti()
