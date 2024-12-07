import sqlite3
from typing import Self
class Database :
    def _init_(self,db):
        self.con = sqlite3 .Connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREAT TABLE IF NOT EXISTS emoloyees (
           id Integer Primary Key, 
           name text,
           age text, 
           job text, 
           email text, 
           gender text ,
           mobile text ,
           address text,
        )
        """
        self.cur.execute (sql) 
        Self.con.commit ()

    def insert(self,name,age,job,email,gender,mobile,address):
        self.cur.execute("insert into employee values (NULL,?,?,?,?,?,?,?)",
                         (name,age,job,email,gender,mobile,address)
        )
        self.con.commit()

    def fetch(self):
        self.cur.execute (" SELECT * FROM employess") 
        rows = self.cur.fetchall ()
        return rows

    def remove(self):
        self.cur.execute("delete from employees where id=?",(id,)) 
        self.con.commit()

    def update(self,name,age,job,email,gender,mobile,address):
        self.cur.execute("update employees set name=?, age=?, job=?, email=?,gender=?, mobile=?, address=? where id=?",
                         )

