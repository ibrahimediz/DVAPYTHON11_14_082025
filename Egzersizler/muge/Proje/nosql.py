# from pymongo.mongo_client import MongoClient
# uri = "mongodb+srv://dvaadmin:12345@appcluster.8lswvog.mongodb.net/?retryWrites=true&w=majority&appName=appCluster"
# # Create a new client and connect to the server
# client = MongoClient(uri)
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# db = client["dva2104"]
# col = db["books"]
# # sonuc = col.insert_one({"ad":"ali","soyad":"veli","yas":20})
# # print(sonuc.inserted_id)


# # print(*col.find({},{"_id":0}))

# for item in col.find({"price":{"$gt":20}},{"_id":0}):
#     print(item.get('title'))

from pymongo import MongoClient

class MongoDBTool:
    def __init__(self,yol,db="dva2104",col="books"):
        self.yol = yol
        self.client = MongoClient(self.yol)
        self.db = self.client[db]
        self.col = self.db[col]

    def insert(self,data):
        sonuc = self.col.insert_one(data)
        return sonuc.inserted_id
    
    def inserts(self,data):
        sonuc = self.col.insert_many(data)
        return sonuc.inserted_ids
    

    def find(self,sorgu,projection=None):
        return list(self.col.find(sorgu,projection))
    

    def delete(self,sorgu):
        return self.col.delete_one(sorgu)
    
    def update(self,sorgu,data):
        return self.col.update_one(sorgu,data)