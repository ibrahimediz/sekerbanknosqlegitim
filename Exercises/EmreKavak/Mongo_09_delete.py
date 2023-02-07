import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["EmreKavak"]
col = db["Musteriler"]

kayit = col.find_one()




sorgu = {"_id":kayit["_id"]}
sonuc = col.delete_one(sorgu)
print(sonuc.deleted_count)