
import sqlite3 as sql

class DBTool():
    def __init__(self,yol):
        self.yol = yol
        self.db = sql.connect(yol)
        self.cur = self.db.cursor()

    def sorgu(self,sorgu):
        return self.cur.execute(sorgu).fetchall()
    
    def insert(self,sorgu):
        self.cur.execute(sorgu)
        self.db.commit()
        return self.cur.lastrowid
    

    def update(self,sorgu):
        self.cur.execute(sorgu)
        self.db.commit()
        return self.cur.rowcount

    def delete(self,sorgu):
        try:
            self.cur.execute(sorgu)
        except:
            self.db.rollback()
        else:
            self.db.commit()
            return self.db.rowcount

    def __del__(self):
        self.cur.close()
        self.db.close()