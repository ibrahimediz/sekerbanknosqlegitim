import pymongo 
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["korkmazDb"]
collName = "musteriler"
col = db[collName]
yenideger = {"$set":{"email":"korkmaz@korkmaz.com"}}
result = col.find({},{"_id":0,"adi":1,"tel":1,"email":1})
print(result)
 

with client:
    db = client.korkmazDb
    liste = db.musteriler.find()
    for item in liste:
        print(item["_id"])
        sorgu = {"_id":{"$eq":item["_id"]}}
        yenideger = {"$set":{"adi":item["adi"].upper()}}
        guncelle = db.musteriler.update_one(sorgu, yenideger)
