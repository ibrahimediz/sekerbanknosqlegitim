import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["EmreKavak"]
col = db["Musteriler"]

kayit = col.find_one()



print(kayit["_id"]) # 63da56eec48f9afb58c18526
sorgu = {"_id":{"$eq":"63da56eec48f9afb58c18526"}}
sonuc = col.delete_one(sorgu)
print(sonuc.deleted_count)
# sorgu = {"_id":kayit["_id"]}
# sonuc = col.delete_one(sorgu)
# print(sonuc.deleted_count)