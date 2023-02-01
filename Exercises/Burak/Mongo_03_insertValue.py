import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "BURAK"
db=client[dbName]
colName = "musteriler"
col=db[colName]
sozluk = {
    "adi":"BURAK",
    "soyadi":"GULBEYAZ",
    "tel":"5554445544",
    "email":"burak@burak.com"
}
res = col.insert_one(sozluk) #### insertOne
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")

