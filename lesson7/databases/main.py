import sqlite3
conn=sqlite3.connect('lesson7/databases/test.db')
cur=conn.cursor()
data=cur.execute("SELECT * FROM users")
print(data.fetchall())
conn.close()