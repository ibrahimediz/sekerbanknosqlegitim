import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "ozge"
db=client[dbName]
colName = "musteriler"
col=db[colName]
sozluk = {
    "adi":"Özge",
    "soyadi":"Şenkul",
    "tel":"5555555",
    "email":"ozge@senkul.com"
}
res = col.insert_one(sozluk) #### insertOne ile tekbir kayıt koleksiyona kaydedildi.
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")
print(res.inserted_id) # 63da5001dce24b978200a634