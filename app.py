#here we will do the things
import database
def create():
    print(f"creating table")
    c,conn=database.conn()
    c.execute("""CREATE TABLE cricketers(rowid SERIAL PRIMARY KEY,first_name text,last_name text,email text) """)
    conn.commit()
    c.close()
    conn.close()
def enter_one(value):
    print(f"entering one item")
    c,conn=database.conn()
    c.execute("INSERT INTO cricketers (first_name,last_name,email) VALUES (%s,%s,%s)",value)
    conn.commit()
    c.close()
    conn.close()

def enter_many(players):
    print(f"entering many at once")
    c,conn=database.conn()
    c.executemany("INSERT INTO cricketers (first_name,last_name,email) VALUES (%s,%s,%s)",players)
    conn.commit()
    c.close()
    conn.close()
def viewall():
    print(f"viewing all before deleting")
    c,conn=database.conn()
    c.execute("SELECT * FROM cricketers")
    yo=c.fetchall()
    for a in yo:
        print(a)
    conn.commit()
    c.close()
    conn.close()
def deleting(rowid):
    print(f"deleting a row 2")
    c,conn=database.conn()
    c.execute("DELETE FROM cricketers WHERE rowid=%s",(rowid,))
    conn.commit()
    c.close()
    conn.close()
def afterdelete():
    print(f"viewing after deleting")
    c,conn=database.conn()
    c.execute("SELECT * FROM cricketers")
    yo=c.fetchall()
    for a in yo:
        print(a)
    conn.commit()
    c.close()
    conn.close()

#calling the methods
value=('sachin','tendulkar','sachin@tendulkar.com')
players=[('sourav','ganguly','sourav@ganguly'),('brian','lara','brian@lara.com'),('ms','dhoni','ms@dhoni.com'),('virat','kohli','virat@kohli.com'),('rohit','sharma','rohit@sharma.com')]
rowid=2
create()
enter_one(value)
enter_many(players)
viewall()
deleting(rowid)
afterdelete()

