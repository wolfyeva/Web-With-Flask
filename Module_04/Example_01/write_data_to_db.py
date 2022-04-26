import sqlite3
con = sqlite3.connect('Module_04\Example_01\myweb.db')
cur = con.cursor()
# Insert a row of data
cur.execute("INSERT INTO user (`name`, `email`, `password`) VALUES ('John','john@gmail.com','333333')")
# Save (commit) the changes
con.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()