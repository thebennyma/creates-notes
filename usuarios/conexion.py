import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="master_python",
        port=3308
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]
