import sqlite3 as sql
from dbTool import DBTool
from nosql import MongoDBTool


yol = r"Egzersizler/cevaplar/Proje/db/chinook.db"
db = DBTool(yol)
nosqldb = MongoDBTool("mongodb+srv://dvaadmin:12345@appcluster.8lswvog.mongodb.net/?retryWrites=true&w=majority&appName=appCluster",
                      db="dva1108Egzersiz",col="cevaplar_tracks")
sorgu = """ SELECT  tr.name,  art.name FROM artists  as art
LEFT JOIN albums as alb ON art.artistid = alb.artistid
LEFT JOIN tracks as tr ON alb.albumid = tr.albumid LIMIT 30"""
sonuclar = db.sorgu(sorgu)

for item in sonuclar:
    data = {"name":item[0],"artist":item[1]}
    print(nosqldb.insert(data),file=open("Egzersizler/cevaplar/Proje/log.csv","a"))