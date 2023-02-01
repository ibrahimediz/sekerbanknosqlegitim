import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "EmreKavak"
db = client[dbName]
collectionName = "Musteriler"
col = db[collectionName]
liste = [{
    "adi":"Emre",
    "soyadi":"Kavak",
    "tel":"15248235",
    "email":"emk@ekadasd.com"
},{
    "adi":"Umut",
    "soyadi":"Kavak",
    "tel":"546125545",
    "email":"umk@ekadasd.com"
}]

res = col.insert_many(liste)
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")