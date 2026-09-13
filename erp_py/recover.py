import sqlite3
conn = sqlite3.connect('ERP.db')
c = conn.cursor()
conn.commit()
x = c.execute("select * from login")
x = c.fetchall()
conn.commit()
print(x)
