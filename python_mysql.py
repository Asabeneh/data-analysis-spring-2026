from mysql.connector import connect
import json


db = connect(
    host='localhost', 
    user='root', 
    password='root'
    )

cursor = db.cursor()

cursor.execute('USE cat_db')

sql = "INSERT INTO cats (id, name, origin, life_span, weight, description, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
values = []
with open('./cats.json') as f:
    data = json.load(f)

    for item in data:
        value = (item['id'], item['name'], item['origin'], item['life_span_average'], item['weight_average'], item['description'], item['image_url'])
        values.append(value)
cursor.executemany(sql, values)
db.commit()

print(f'===== {len(values)} cats have been inserted in to cats table ====')





'''
What is our sources of data:
API 
Databases
Scraped from websites



'''
