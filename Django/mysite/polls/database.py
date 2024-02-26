import pymysql.cursors

class Database:
    def __init__(self):
        pass
    def crud(self,args):
        try:
            connection = pymysql.connect(host='localhost',
                                         user='user',
                                         password='User123456789',
                                         database='s203_revisão_poo',
                                         charset='utf8mb4',
                                         autocommit=True
                                         )
            with connection.cursor() as cursor:
                try:
                    cursor.execute(args)
                    return cursor.fetchall()
                except Exception as e:
                    return f"erro :{e}"
                finally:
                    connection.close()

        except Exception as e:
            print(f"erro : {e}")


