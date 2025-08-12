import sqlite3 as sql
from dbTool import DBTool
from nosql import MongoDBTool


yol = r"Dokumanlar\Proje\db\chinook.db"
db = DBTool(yol)
nosqldb = MongoDBTool("mongodb+srv://dvaadmin:12345@appcluster.8lswvog.mongodb.net/?retryWrites=true&w=majority&appName=appCluster",
                      db="dva1108Egzersiz",col="mccakmak")
sorgu = """ SELECT tr.trackid, tr.name, alb.title, art.name FROM artists  as art
LEFT JOIN albums as alb ON art.artistid = alb.artistid
LEFT JOIN tracks as tr ON alb.albumid = tr.albumid"""
sonuclar = db.sorgu(sorgu)

for item in sonuclar:
    data = {"trackid":item[0],"name":item[1],"album":item[2],"artist":item[3]}
    print(nosqldb.insert(data),file=open("log.csv","a"))
    

