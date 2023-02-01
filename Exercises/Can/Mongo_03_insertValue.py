import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "candb"
db=client[dbName]
colName = "musteriler"
col=db[colName]
sozluk = {
    "adi":"İbrahim",
    "soyadi":"EDİZ",
    "tel":"5554635",
    "email":"ediz@ibrahimediz.com"
}
res = col.insert_one(sozluk) #### insertOne
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")