import pymysql

def get_connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="admin",
            password="ciel",
            database="securite",
            port=3316,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print("Erreur MySQL :", e)
        return None