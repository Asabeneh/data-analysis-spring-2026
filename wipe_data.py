from mysql.connector import connect

db = connect(
    host='localhost', 
    user='root', 
    password='root'
    )

cursor = db.cursor()

cursor.execute('USE cat_db')

cursor.execute('TRUNCATE TABLE cats')
print('===== Data has been wipped out ====')