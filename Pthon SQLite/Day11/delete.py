import sqlite3
conn=sqlite3.connect('new.db')
c=conn.cursor()

c.execute('delete from record  where age=13')
conn.commit()

c.execute('SELECT * FROM record')

emp2=c.fetchall()
for i in emp2:
    print (i)

conn.close()