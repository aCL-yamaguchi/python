import mysql.connector

conn  = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='luxav2',
)

connected = conn.is_connected()
print(connected)
if (not connected):
    print("not conneted")

cur = connect.cursor()

sql = "select * from deal;"
cur.execute(sql)

for row in cur.fetchall():
    print(row[0], row[1])

cur.close
conn.close
