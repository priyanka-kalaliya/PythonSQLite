import sqlite3
conn=sqlite3.connect('demo.db')
c=conn.cursor()
c.execute('CREATE TABLE if not exists bank(name text, balance int)')

for i in range (5):
    a=input('enter name: ')
    b=int(input('enter balance: '))

    c.execute("insert into bank values(?,?)",(a,b))

# c.execute("insert into record values('xyz','13')")
conn.commit()
conn.close