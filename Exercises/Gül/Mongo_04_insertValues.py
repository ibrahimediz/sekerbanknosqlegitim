import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "GTSC"
db = client[dbName]
collectionName = "Musteriler"
col = db[collectionName]
liste = [{
    "adi":"Elif",
    "soyadi":"Taşçı",
    "tel":"15248235",
    "email":"el@elf.com"
},{
    "adi":"Gülce",
    "soyadi":"Tascı",
    "tel":"546125545",
    "email":"umk@ekadasd.com"
}]

res = col.insert_many(liste)
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")