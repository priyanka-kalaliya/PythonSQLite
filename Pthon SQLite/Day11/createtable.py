import sqlite3
conn=sqlite3.connect('new.db')
c=conn.cursor()
c.execute('CREATE TABLE if not exists record(name text, age int)')

for i in range (3):
    a=input('enter name')
    b=int(input('enter age:'))

    c.execute("insert into record values(?,?)",(a,b))

# c.execute("insert into record values('xyz','13')")
conn.commit()
conn.close