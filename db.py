import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="123456", host="localhost", port="5432")
cursor = conn.cursor()
sql = "select * from source_relation"
cursor.execute(sql)
data = cursor.fetchall()
cursor.close()
conn.close()
for item in data:
    id = item[0]
    name = item[1]
    code = item[2]
    print(id, name, code)
