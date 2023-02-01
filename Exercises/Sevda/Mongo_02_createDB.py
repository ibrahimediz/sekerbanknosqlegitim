import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
ndb=client["Sevda"]
ncol=ndb["Musteriler"]
ndict= {
    "adi":"sevda",
    "soyadi":"akyuz"
}
ncol.insert_one(ndict)
print(*client.list_database_names())
print(*ndb.list_collection_names())

