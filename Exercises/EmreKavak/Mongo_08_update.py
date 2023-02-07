import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["EmreKavak"]
col = db["Musteriler"]


result = col.find()
for item in result:
        print(item["_id"])
        sorgu = {"_id":{"$eq":item["_id"]}}
        yenideger = {"$set":{"adi":item["adi"].upper()}}
        guncelle = db.Musteriler.update_one(sorgu, yenideger)
        print(guncelle.modified_count)
    