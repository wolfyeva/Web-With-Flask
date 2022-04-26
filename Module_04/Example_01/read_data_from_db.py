import sqlite3
con = sqlite3.connect('Module_04\Example_01\myweb.db')
cur = con.cursor()
querydata = cur.execute('SELECT * FROM user ORDER BY id')
for row in querydata:
    print(row)
con.close
