import sqlite3
con = sqlite3.connect('Module_04\Example_01\myweb.db')
cur = con.cursor()
# querydata = cur.execute('SELECT * FROM user ORDER BY id')
querydata = cur.execute('SELECT * FROM user WHERE `email`="benctw2@gmail.com"')
results = cur.fetchall()
if results:
    print('ok')
    print(results[0])

# for row in querydata:
#     print(row)
con.close
