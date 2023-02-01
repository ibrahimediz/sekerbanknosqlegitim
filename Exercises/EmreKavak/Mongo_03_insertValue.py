import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "EmreKavak"
db = client[dbName]
collectionName = "Musteriler"
col = db[collectionName]
sozluk = {
    "adi":"Emre",
    "soyadi":"Kavak",
    "tel":"15248235",
    "email":"emk@ekadasd.com"
}

res = col.insert_one(sozluk)
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")