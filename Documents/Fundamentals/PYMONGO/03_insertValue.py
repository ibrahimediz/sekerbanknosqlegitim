import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "ediz"
db=client[dbName]
colName = "musteriler"
col=db[colName]
sozluk = {
    "adi":"İbrahim1",
    "soyadi":"EDİZ",
    "tel":"5554635",
    "yas":40,
    "email":"ediz@ibrahimediz.com"
} # döküman
res = col.insert_one(sozluk) #### insertOne ile tekbir kayıt koleksiyona kaydedildi.
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")
print(res.inserted_id) # 63da5001dce24b978200a634

