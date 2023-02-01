import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "KEREMDB"
db=client[dbName]
colName = "MUSTERILER"
col=db[colName]
sozluk = {
     "adi":"Kerem",
    "soyadi":"Şentürk",
    "tel":"5303462869",
    "email":"nkeremsenturk@gmail.com"
}
res = col.insert_one(sozluk) #### insertOne
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")