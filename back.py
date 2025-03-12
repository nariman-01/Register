import sqlite3
class Exam():
    def __init__(self,adress):
        self.con = sqlite3.connect(adress)
        self.cur = self.con.cursor()
    def create_table(self):
        self.cur.execute("create table if not exists person (id integer primary key,fname text,lname text,email text,password text)")
        self.con.commit()
    def insert(self,name,family,email,pas):
        self.cur.execute("insert into person values (NULL,?,?,?,?)",(name,family,email,pas))
        self.con.commit()
    def read(self):
        self.cur.execute("select * from person")
        self.con.commit()
        return self.cur.fetchall()


    
        