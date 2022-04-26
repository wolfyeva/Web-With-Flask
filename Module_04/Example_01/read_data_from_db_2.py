import sqlite3
con = sqlite3.connect('Module_04\Example_01\myweb.db')
cur = con.cursor()
cur.execute('SELECT * FROM user ORDER BY id')
result = cur.fetchall()
for row in result:
    print(row)
con.close
