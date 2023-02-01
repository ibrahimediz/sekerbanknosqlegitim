import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "Anil"
db = client[dbName]
collectionName = "Musteriler"
col = db[collectionName]
liste = [{
    "adi":"Can",
    "soyadi":"Deniz",
    "tel":"15248235",
    "email":"can@deniz.com"
},{
    "adi":"Asya",
    "soyadi":"Güneş",
    "tel":"546125545",
    "email":"asy@gunes.com"
}]

res = col.insert_many(liste)
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")