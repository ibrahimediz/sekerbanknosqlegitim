import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

with client:
    db = client.ozge
    liste = db.musteriler.find()
    for item in liste:
        print(item["_id"])
        sorgu = {"_id":{"$eq":item["_id"]}}
        yenideger = {"$set":{"adi":item["adi"].upper()}}
        guncelle = db.musteriler.update_one(sorgu, yenideger)