import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

with client:
    db=client.Sevda
    res = db.Musteriler.find_one()
    print(res["_id"])
    sorgu = {"_id":{"$eq":res["_id"]}}
    sonuc = db.Musteriler.delete_one(sorgu)