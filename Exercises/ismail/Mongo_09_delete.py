import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db=client["korkmazDb"]
col=db["musteriler"]

sorgu = {"adi":{"$eq":"EGE"}}
sonuc = col.delete_one(sorgu)
print(sonuc.deleted_count)