import mysql.connector
# Establishing connection to database
try:
    conn = mysql.connector.connect(
       user="root", database="clinic_database"
    )
except Exception as e:
    print("Exception : ",e)
#Creating database object
class clinic_database:
    def __init__(self) -> None:
        self.cursor=conn.cursor()
    def view_table(self,table_name) -> None:
        self.cursor.execute("select * from "+table_name+";")
